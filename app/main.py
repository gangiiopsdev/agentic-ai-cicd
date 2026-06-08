from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_host(host):
    return ''.join(char if char.isalnum() or char in '.-' else '_' for char in host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    subprocess.call(["ping", escaped_host])
    return {"status": "completed"}