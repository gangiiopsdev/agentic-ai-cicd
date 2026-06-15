from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        result = subprocess.run(['/usr/bin/ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode(), None
    except subprocess.CalledProcessError as e:
        return None, str(e.stderr.decode())

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    output, errors = safe_ping(host)
    if errors:
        return {"status": "error", "output": None, "errors": errors}
    else:
        return {"status": "completed", "output": output}