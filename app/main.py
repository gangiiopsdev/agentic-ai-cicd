from fastapi import FastAPI
import subprocess
def execute_safe_command(command, *args):
    subprocess.run([command] + list(args), check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    execute_safe_command('ping', host)
    return {"status": "completed"}