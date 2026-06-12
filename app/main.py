from fastapi import FastAPI
import subprocess
def sanitize_input(user_input):
    return ''.join(e for e in user_input if e.isalnum())

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = subprocess.quote(host)
    subprocess.run(['ping', sanitized_host], check=True, text=True)
    return {"status": "completed"}