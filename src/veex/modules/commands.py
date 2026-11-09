import uuid
import string
import secrets
import subprocess

from google.genai import Client, errors
from dotenv import load_dotenv

import os

load_dotenv()

client = Client(api_key=os.getenv("AI_API_KEY"))

# Handleres
def exit(user_input=None):
    raise SystemExit

def password(input):
    input_arr = input.split()

    if ( len(input_arr) < 2 ) or ( not input_arr[1].isdigit() ):
        print("Password length not included or invalid input")
        return

    length = input_arr[1]
    length = int(length)
    chars = string.ascii_letters + string.digits + "!@#$%^&*"

    return ''.join(secrets.choice(chars) for _ in range(length))

def ai(user_input):
    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=user_input
        )

        return response.text
    except errors.APIError as e:
        print(f"Encountered API error: {e}")

def help(user_input=None):
    for name, command in commands.items():
        print(f"{name:<12} {command['description']}")
        print(f"{'':12} Usage: {command['usage']}")

def clear(user_input=None):
    command = 'cls' if os.name == 'nt' else 'clear'
    subprocess.run(command, shell=True)

def gen_uuid(user_input=None):
    return uuid.uuid4()

# Functions

def get_commands():
    return commands

def is_command(name):
    words = name.split()

    if words and words[0].lower() in commands:
        return True, commands[words[0].lower()]

    return False, None

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
    },

    "uuid": {
        "function": gen_uuid,
        "description": "generates a random UUID",
        "usage": "uuid"
    },
}
