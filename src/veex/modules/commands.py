import uuid
import string
import secrets

# Handleres
def exit():
    print("exited")
    raise SystemExit

def password(length=24):
    length = int(length)
    chars = string.ascii_letters + string.digits + "!@#$%^&*"

    return ''.join(secrets.choice(chars) for _ in range(length))

# Commands Table
commands = {
    "exit": exit,
    "password": password
}

# Functions

def get_commands():
    return commands

def is_command(name):
    words = name.split()

    if words and words[0].lower() in commands:
        return True, commands[words[0].lower()]

    return False, None
