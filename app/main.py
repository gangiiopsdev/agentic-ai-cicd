from fastapi import FastAPI
import subprocess
def sanitize_input(user_input):
    return ''.join(filter(str.isalnum, user_input))

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    host = sanitize_input(host)
    result = subprocess.run(['/usr/bin/ping', '-c', '1', host], capture_output=True, text=True, check=True)
    return {"status": "completed", "output": result.stdout}