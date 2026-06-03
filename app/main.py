from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str) -> bool:
    try:
        host = shlex.quote(host)
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return True, output.stdout
    except subprocess.CalledProcessError as e:
        return False, str(e.stderr)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    success, output = safe_ping(host)
    if success:
        return {"status": "completed", "output": output}
    else:
        return {"status": "failed", "error": output}