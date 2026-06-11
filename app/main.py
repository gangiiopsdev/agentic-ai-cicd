from fastapi import FastAPI
import subprocess
def generate_ping_command(host: str) -> str:
    return f'ping {host}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        subprocess.run(generate_ping_command(host).split(), check=True, shell=False)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}