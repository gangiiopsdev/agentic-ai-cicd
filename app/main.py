from fastapi import FastAPI
import subprocess

generate_ping_command = lambda host: f'ping {host}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = subprocess.run(generate_ping_command(host), shell=False, capture_output=True, text=True)
        return {"status": "completed", "stdout": result.stdout, "stderr": result.stderr}
    except Exception as e:
        return {"status": "failed", "error": str(e)}