from fastapi import FastAPI
import subprocess
def run_safe_command(command, *args):
    return subprocess.run([command] + list(args), check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = run_safe_command("ping", host)
    return {"status": "completed", "stdout": result.stdout.decode() if result.stdout else None}