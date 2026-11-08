--AI Was used to help make the README

# VEEX

VEEX is a lightweight terminal-based Python CLI for quick utility commands and Gemini-powered AI interaction.

Version: v0.1.0

## Features

- Password generation
- UUID generation
- Terminal clear command
- Built-in help command
- AI command using Gemini
- Simple interactive CLI loop

## Usage

Run the CLI:

```bash
uv run veex
```

Or:

```bash
python -m veex
```

## Commands

| Command | Description | Usage |
| --- | --- | --- |
| `exit` | Exits the CLI | `exit` |
| `password` | Generates a random password | `password [length]` |
| `ai` | Sends a prompt to Gemini and prints the response | `ai [message]` |
| `help` | Lists all commands and their usage | `help` |
| `clear` | Clears the terminal | `clear` |
| `uuid` | Generates a UUID | `uuid` |

## Gemini API configuration

This project loads the API key from an environment variable named `AI_API_KEY`.

Create a `.env` file in the project root:

```env
AI_API_KEY=your_api_key_here
```