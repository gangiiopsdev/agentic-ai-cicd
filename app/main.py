from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_host(host: str):
    return host.replace(';', '').replace('&', '')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    subprocess.call(["ping", escaped_host])
    return {"status": "completed"}