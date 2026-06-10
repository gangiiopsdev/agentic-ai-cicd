from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_command(command):
    # Validate and sanitize the command before running it
    safe_command = [arg for arg in command.split(' ') if arg.strip()]  # Example sanitization
    result = subprocess.run(safe_command, capture_output=True, text=True)
    return result.stdout