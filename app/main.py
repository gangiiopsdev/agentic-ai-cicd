from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str) -> str:
    # Sanitize the host input to avoid shell injection attacks
    safe_host = shlex.quote(host)
    return f'ping {safe_host}'

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        output = subprocess.run(safe_ping(host), capture_output=True, text=True, check=True, shell=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}