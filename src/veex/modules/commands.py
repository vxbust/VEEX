import uuid
import string
import secrets
import subprocess

from google.genai import Client
from dotenv import load_dotenv

import os

load_dotenv()

client = Client(api_key=os.getenv("AI_API_KEY"))

# Handleres
def exit(user_input=None):
    print("exited")
    raise SystemExit

def password(input):
    length = input.split()[1]
    length = int(length)
    chars = string.ascii_letters + string.digits + "!@#$%^&*"

    return ''.join(secrets.choice(chars) for _ in range(length))

def ai(user_input):
    return f''' Gemini: {client.models.generate_content(
        model="gemini-3.6-flash",
        contents=user_input
    ).text} '''

def help(user_input=None):
    print("Commands: \n")
    for name, dict in commands.items():
        print(f"{name} - {dict["description"] or "no description"}, \n  Usage: {dict["usage"] or ""} \n")

def clear(user_input=None):
    command = 'cls' if os.name == 'nt' else 'clear'
    subprocess.run(command, shell=True)

# Commands Table
commands = {
    "exit": {
        "function": exit,
        "description": "Ends the cli",
        "usage": "exit"
    },

    "password": {
        "function": password,
        "description": "generates a random password",
        "usage": "password [length]"
    },
    
    "ai": {
        "function": ai,
        "description": "calls gemini api and outputs the response",
        "usage": "ai [message]"
    },

    "help": {
        "function": help,
        "description": "returns a list of all commands and their description",
        "usage": "help"
    },

    "clear": {
        "function": clear,
        "description": "clears the terminal",
        "usage": "clear"
    }
}

# Functions

def get_commands():
    return commands

def is_command(name):
    words = name.split()

    if words and words[0].lower() in commands:
        return True, commands[words[0].lower()]

    return False, None
