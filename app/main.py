from fastapi import FastAPI
import subprocess
def generate_ping_command(host): return f'ping {host}'
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    # Safe implementation
    if '&&' in host or ';' in host:
        raise ValueError("Invalid input")
    subprocess.call(generate_ping_command(host), shell=False)
    return {"status": "completed"}