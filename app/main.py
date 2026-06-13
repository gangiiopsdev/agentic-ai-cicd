from fastapi import FastAPI
import subprocess
def execute_safe_command(command: str, *args):
    return subprocess.run(command.format(*args), check=True, shell=False)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        execute_safe_command(f'ping {host}', host)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}