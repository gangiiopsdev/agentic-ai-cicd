from fastapi import FastAPI
import subprocess
import shlex
def shell_safe(host):
    return all(c.isalnum() or c in '.:-' for c in host)

app = FastAPI()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not shell_safe(host):
        return {"status": "error", "message": "Invalid host name"}
    try:
        output = subprocess.run(['ping', shlex.quote(host)], timeout=5, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": output.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e.stderr.decode())}