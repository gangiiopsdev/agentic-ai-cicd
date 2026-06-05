from fastapi import FastAPI
import subprocess
gt
app = FastAPI()

gt
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

gt
@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and explicit argument list
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr.decode()}
gt