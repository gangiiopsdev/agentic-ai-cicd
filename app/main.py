from fastapi import FastAPI
import subprocess
def shellquote(text):
    return ''.join(c if c.isalnum() or c in '_.-/' else f'\{ord(c):o:03}' for c in text)

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_host = shellquote(host)
    subprocess.call(['ping', safe_host])
    return {"status": "completed"}