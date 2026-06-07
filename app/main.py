from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        output = subprocess.check_output([quote('ping'), quote(host)], stderr=subprocess.STDOUT, text=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}

# Recommended changes to mitigate the risk of command injection
@app.get("/ping")
def ping(host: str):
    safe_host = quote(host, safe='')  # Sanitize user input
    try:
        output = subprocess.check_output([quote('ping'), safe_host], stderr=subprocess.STDOUT, text=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}