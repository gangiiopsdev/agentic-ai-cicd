from fastapi import FastAPI
import subprocess
def escape_host(host):
    # Escape any special characters that could alter the command
    return host.replace(';', '').replace('&', '').replace('|', '')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input sanitization
    subprocess.run(['ping', escape_host(host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed"}