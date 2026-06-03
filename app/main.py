from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    subprocess.run(['ping', '-c', '1', host], check=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_safe(host: str):
    try:
        result = ping(host)
        return {"status": "completed", "result": result}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}