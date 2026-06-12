from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host to prevent command injection
    if not host.replace('.', '').isdigit() and not ('-' in host or '_' in host):
        return {"status": "failed", "error": "Invalid host format"}
    try:
        result = subprocess.run(['ping'] + shlex.split(host), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "stdout": result.stdout.decode(), "stderr": result.stderr.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}