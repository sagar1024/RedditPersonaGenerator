import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

#Use the newer, faster model
model = genai.GenerativeModel(model_name="models/gemini-2.5-flash")

def build_prompt(username, data):
    content = ""

    for post in data["posts"]:
        if post["text"]:
            content += f"POST: {post['text']}\nURL: {post['url']}\n\n"

    for comment in data["comments"]:
        content += f"COMMENT: {comment['text']}\nURL: {comment['url']}\n\n"

    return f"""

    You are an AI UX researcher. Based on the Reddit posts and comments below, create a structured user persona.

    FORMAT:
    NAME: {username}
    AGE:
    OCCUPATION:
    STATUS:
    LOCATION:
    ARCHETYPE:
    PERSONALITY:
    MOTIVATIONS:
    BEHAVIORS & HABITS:
    FRUSTRATIONS:
    GOALS & NEEDS:
    CITATIONS: Mention Reddit URLs used to infer each section.

    DATA:
    {content}
    
    Note -
        1. describe the persona with one or two word at the top
        2. please don't put BOLD letters in the response
        3. put the citations in the end after writing the persona """

def generate_persona(username, data):
    prompt = build_prompt(username, data)

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating persona: {e}"
    