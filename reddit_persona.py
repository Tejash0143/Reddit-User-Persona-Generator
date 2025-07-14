import requests
import os
import json
from urllib.parse import urlparse
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
HEADERS = {"User-Agent": "UserPersonaBot/1.0"}


def extract_username(url):
    """
    Extracts the Reddit username from a profile URL.
    Example: https://www.reddit.com/user/kojied/ -> kojied
    """
    parsed = urlparse(url)
    parts = parsed.path.strip("/").split("/")
    if len(parts) >= 2 and parts[0] == "user":
        return parts[1]
    return None


def get_user_content(username):
    """
    Fetches comments and submissions from Reddit user profile (public endpoints).
    """
    base_url = f"https://www.reddit.com/user/{username}/"
    posts_url = f"{base_url}submitted.json"
    comments_url = f"{base_url}comments.json"

    print(f"🔍 Fetching posts/comments for: {username}")

    posts = requests.get(posts_url, headers=HEADERS).json()
    comments = requests.get(comments_url, headers=HEADERS).json()

    post_texts = [p["data"]["title"] + " " + p["data"].get("selftext", "")
                  for p in posts.get("data", {}).get("children", [])]

    comment_texts = [c["data"]["body"]
                     for c in comments.get("data", {}).get("children", [])]

    return "\n".join(post_texts + comment_texts)


def generate_persona(text):
    """
    Sends content to Together API to generate a user persona.
    """
    print("🧠 Generating persona using Together AI...")

    response = requests.post(
        "https://api.together.xyz/v1/completions",
        headers={
            "Authorization": f"Bearer {TOGETHER_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
            "prompt": f"Based on the following Reddit posts and comments, generate a detailed persona of the user:\n\n{text}",
            "max_tokens": 512,
            "temperature": 0.7
        }
    )

    full_response = response.json()
    print("📦 Full API Response:", json.dumps(full_response, indent=2))

    return full_response["choices"][0]["text"]


def main():
    url = input("Enter Reddit Profile URL: ").strip()
    username = extract_username(url)

    if not username:
        print("❌ Could not extract username from URL.")
        return

    content = get_user_content(username)

    if not content:
        print("⚠️ No content found for user.")
        return

    persona = generate_persona(content)

    filename = f"{username}_persona.txt"
    with open(filename, "w") as f:
        f.write(persona.strip())

    print(f"✅ Persona saved as {filename}")


if __name__ == "__main__":
    main()
