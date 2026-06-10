from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return ping(host)