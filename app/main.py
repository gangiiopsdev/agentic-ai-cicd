from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Use an absolute path for the command to mitigate injection risks
        result = subprocess.run(['/usr/bin/ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {
            "status": "completed",
            "output": result.stdout.decode()
        }
    except subprocess.CalledProcessError as e:
        return {
            "status": "error",
            "output": str(e)
        }