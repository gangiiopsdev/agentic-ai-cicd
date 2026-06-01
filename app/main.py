from fastapi import FastAPI
import subprocess

def execute_command(command: str):
    try:
        result = subprocess.run(command.split(), capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Command failed with exit code {e.returncode}: {e.stderr}"

def sanitize_input(input_string: str) -> str:
    # Implement input sanitization logic here
    return ''.join(c for c in input_string if c.isalnum())  # Example of basic sanitization

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if ' ' not in sanitized_host and '.' in sanitized_host:  # Basic format check for IP or domain
        command = f'ping {sanitized_host}'
        output = execute_command(command)
        return {"status": "completed", "output": output}
    else:
        return {"error": "Invalid input"}