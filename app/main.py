from fastapi import FastAPI
import subprocess
def escape_shell_arg(arg):
    return ' '.join(map(shlex.quote, arg.split()))

def validate_host(host):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
    if not all(char in allowed_chars for char in host):
        raise ValueError("Invalid hostname")

app = FastAPI()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    escaped_host = escape_shell_arg(host)
    try:
        result = subprocess.run(['ping', '-c 1', escaped_host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}