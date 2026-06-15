from fastapi import FastAPI
import subprocess
def escape_command(args):
    return [subprocess.list2cmdline(arg) for arg in args]

app = FastAPI()

def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(char for char in input_str if char in allowed_chars)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    result = subprocess.run(escape_command(['ping', sanitized_host]), capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}