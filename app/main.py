from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: f'ping {host}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    subprocess.run(generate_ping_command(host).split(), check=True, shell=False)
    return {"status": "completed"}