from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    try:
        # Using a whitelist of allowed hosts or implementing proper validation
        if host in ['google.com', 'example.com']:
            cmd = shlex.split('ping ' + host)
            result = subprocess.run(cmd, check=True, capture_output=True, text=True)
            return {"status": "completed", "output": result.stdout}
        else:
            return {"status": "failed", "error": "Host not allowed"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)