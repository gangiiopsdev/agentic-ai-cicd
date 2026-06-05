from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    allowed_hosts = ["example.com", "test.com"]  # Replace with actual list of allowed hosts
    if host not in allowed_hosts:
        return {"status": "error", "error": "Host not allowed"}
    try:
        result = subprocess.run(['ping', shlex.quote(host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "error": str(e)}