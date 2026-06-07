from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(user_input):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-:_/\~()[]{}<>@#$%^&*+=?`
    return ''.join(filter(allowed_chars.__contains__, user_input))

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    host = sanitize_input(host)
    try:
        subprocess.call(f'ping {host}', shell=False, check=True)
        return {"status": "completed", "message": "Ping successful"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}