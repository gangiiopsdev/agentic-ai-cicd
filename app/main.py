from fastapi import FastAPI
import subprocess
generate_safe_ping_command = lambda host: f"ping {host.replace(' ', '_') if ' ' in host else host}"

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    subprocess.call(generate_safe_ping_command(host), shell=False)
    return {"status": "completed"}