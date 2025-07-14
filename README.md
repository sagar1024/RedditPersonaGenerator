# Reddit Persona Generator

Reddit Persona Generator is an application that scrapes Reddit user data and generates a structured user persona using Google Gemini 2.5 Flash.

## Features

1. Scrapes posts and comments from any public Reddit user profile
2. Uses Google Gemini API to generate a structured user persona
3. Persona output includes sections like name, occupation, motivations, behaviors, and citations.
4. Simple and intuitive Streamlit web interface
5. Output is downloadable as a text file

## Setup Instructions

1. Clone the repository:

```
bash
git clone https://github.com/sagar1024/RedditPersonaGenerator.git
cd RedditPersonaGenerator
```

2. Install dependencies:

```
bash
pip install -r requirements.txt
```

3. Create a .env file and fill in your API keys: Reddit API keys (from https://www.reddit.com/prefs/apps), Gemini API key (from https://aistudio.google.com/apikey)

4. Run the application:

```
bash
streamlit run app.py
```

## How It Works

1. You enter a Reddit username or profile URL into the app.
2. The app fetches the user’s recent posts and comments using PRAW (Reddit API).
3. It constructs a detailed prompt and sends it to the Gemini API.
4. Gemini returns a persona in plain text format, with attributes inferred from the data.
5. The persona is displayed in the app and can be downloaded as a .txt file.


## Requirements

1. Python 3.8+
2. Reddit API credentials
3. Gemini API key

## Output Example

#### A generated persona file includes:

1. Name
2. Age
3. Occupation
4. Status
5. Location
6. Archetype
7. Personality
8. Motivations
9. Behaviors and Habits
10. Frustrations
11. Goals and Needs
12. Citations with Reddit post or comment URLs

## License
This project is for educational and demonstration purposes only.

## Developed by - SAGAR GURUNG
