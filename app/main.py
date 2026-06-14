from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Using subprocess.run instead of subprocess.call for better security
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "stdout": result.stdout.decode(), "stderr": result.stderr.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "stderr": str(e)}