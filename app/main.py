from fastapi import FastAPI
import subprocess

def generate_ping_command(host):
    if isinstance(host, str) and all(c.isalnum() or c in ('.', '-', '_') for c in host):
        return ['ping', host]
    else:
        raise ValueError('Invalid hostname')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = generate_ping_command(host)
    subprocess.run(command, check=True, shell=False)
    return {"status": "completed"}