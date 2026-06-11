from fastapi import FastAPI
import subprocess
def escape_command(input):
    return ''.join(c if c.isalnum() or c in ['-', '.', '_', '~', ':'] else '_' for c in input)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_command(host)
    subprocess.call(f'ping {escaped_host}')
    return {"status": "completed"}