from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    host = shlex.quote(host)
    return subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = safe_ping(host)
        if result.returncode == 0:
            return {"status": "Success", "output": result.stdout}
        else:
            return {"status": "Failure", "output": result.stderr}
    except subprocess.CalledProcessError as e:
        return {"status": "Failure", "output": str(e)}