from fastapi import FastAPI
import subprocess
generate_ping_command = lambda h: f'ping {h}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = subprocess.run(generate_ping_command(host), shell=True, check=True)
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr.decode()}
    return {"status": "completed", "output": result.stdout.decode()}