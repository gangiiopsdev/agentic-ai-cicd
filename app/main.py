from fastapi import FastAPI
import subprocess
def escape_user_input(user_input):
    return ''.join(c for c in user_input if c.isalnum() or c in '._-')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    safe_host = escape_user_input(host)
    subprocess.call(["ping", safe_host])
    return {"status": "completed"}