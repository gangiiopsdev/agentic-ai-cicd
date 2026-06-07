from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_input(value):
    return ''.join(char for char in value if char.isalnum() or char == '.')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = escape_input(host)
    args = ['ping', sanitized_host]
    subprocess.call(args, shell=False)
    return {"status": "completed"}