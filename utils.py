import re
import os

def extract_username(url_or_name):
    if "reddit.com/user/" in url_or_name:
        match = re.search(r"reddit\.com/user/([^/]+)/?", url_or_name)
        return match.group(1) if match else None
    return url_or_name.strip()

def save_persona_to_file(username, persona):
    os.makedirs("output", exist_ok=True)
    with open(f"output/{username}_persona.txt", "w", encoding="utf-8") as f:
        f.write(persona)
