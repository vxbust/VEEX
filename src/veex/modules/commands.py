import uuid
import string
import secrets

from google.genai import Client
from dotenv import load_dotenv

import os

load_dotenv()

client = Client(api_key=os.getenv("AI_API_KEY"))

# Handleres
def exit():
    print("exited")
    raise SystemExit

def password(input):
    length = input.split()[1]
    length = int(length)
    chars = string.ascii_letters + string.digits + "!@#$%^&*"

    return ''.join(secrets.choice(chars) for _ in range(length))

def ai(question):
    return f''' Gemini: {client.models.generate_content(
        model="gemini-3.6-flash",
        contents=question
    ).text} '''


# Commands Table
commands = {
    "exit": exit,
    "password": password,
    "ai": ai
}

# Functions

def get_commands():
    return commands

def is_command(name):
    words = name.split()

    if words and words[0].lower() in commands:
        return True, commands[words[0].lower()]

    return False, None
