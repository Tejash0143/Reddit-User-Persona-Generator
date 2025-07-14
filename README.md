# Reddit-User-Persona-Generator
A Python-based web app that generates detailed user personas from Reddit profiles using AI. Just enter a Reddit username, and the app fetches the user's post and comment history, analyzes the content, and creates a descriptive persona using a large language model. Built with Python, Streamlit, and the Together API.

## 🚀 Features

- ✅ Extracts username from any Reddit profile URL
- 🔍 Fetches posts and comments via Reddit's public API
- 🧠 Sends content to Together AI for persona generation
- 💾 Saves generated persona to a `.txt` file

---

## 📦 Requirements

- Python 3.7+
- A [Together AI](https://www.together.ai/) API key
- Reddit account with public posts/comments

---

## 🛠️ Setup

### 1. Clone the Repository 
git clone https://github.com/your-username/reddit-user-persona.gitcd reddit-user-persona.

### 2. Create a Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Add API Key to .env
Create a .env file in the project root and add your Together API key:

TOGETHER_API_KEY=your_together_api_key_here


## ▶️ Usage

python reddit_persona.py
You will be prompted to enter a Reddit profile URL:

Enter Reddit Profile URL: https://www.reddit.com/user/kojied/
If successful, the generated persona will be saved as:

kojied_persona.txt


## 📁 File Structure

reddit-user-persona/
│
├── reddit_persona.py       # Main script
├── .env                    # API key (not committed)
├── kojied_persona.txt      # Example output
├── requirements.txt        # Python dependencies
└── README.md               # You are here

## 📚 Example Output (Truncated)

Yeah, I'm not so sure about it. But I just read that the airline is considering this.

I'm interested in space travel, but I don’t have the means yet.
...

## 📌 Notes

Reddit content is fetched anonymously — no API credentials required for Reddit.
Works only for public Reddit accounts with available posts or comments.
Together AI usage is subject to rate limits and token quota.

## 📃 License

This project is licensed under the MIT License.

## 🙌 Acknowledgements

Together AI
Reddit Public API

---

### ✅ Also Add This `requirements.txt`

```txt
requests
python-dotenv


