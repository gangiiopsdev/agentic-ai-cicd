from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/)")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        result = subprocess.run(['ping', host], check=True, shell=False, capture_output=True, text=True)
        return {"host": host, "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"host": host, "error": e.stderr}