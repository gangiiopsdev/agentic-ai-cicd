from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(user_input):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_ '
    return ''.join(c for c in user_input if c in allowed_chars)

def safe_ping(host):
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, timeout=10)
        return output.decode()
    except subprocess.CalledProcessError as e:
        return e.output.decode()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        output = safe_ping(sanitized_host)
        return {"status": "completed", "output": output}
    except Exception as e:
        return {"status": "error", "output": str(e)}