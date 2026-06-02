from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_command(user_input):
    return ''.join(char for char in user_input if char.isalnum() or char.isspace())

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    # Secure implementation using subprocess.Popen with input validation
    escaped_host = escape_shell_command(host)
    args = ['ping', escaped_host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {"status": result.stdout}