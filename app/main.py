from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    generate_ping_command = ['ping', host]
    # Validate the host input to ensure it does not contain malicious content
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    subprocess.call(generate_ping_command)
    return {'status': 'completed'}

def is_valid_host(host: str) -> bool:
    # Simple validation, in production use a more comprehensive check
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return all(char in allowed_chars for char in host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return ping(host)