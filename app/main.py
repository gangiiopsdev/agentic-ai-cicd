from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host or not isinstance(host, str) or len(host.strip()) == 0:
        return {"error": "Invalid input"}
    # Secure implementation
    try:
        subprocess.run(['ping'] + shlex.split(host), check=True)
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}
    return {"status": "completed"}