from fastapi import FastAPI
import subprocess
def escape_command(command):
    return [arg.strip() for arg in command.split()]

def safe_ping(host: str):
    valid_hosts = ['example.com', 'test.net']
    if host not in valid_hosts:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        subprocess.call(escape_command(f'ping {host}'))
    except Exception as e:
        return {"error": str(e)}
    return {"status": "completed"}