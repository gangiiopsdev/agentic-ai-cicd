from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host or len(host) > 255:
        return None
    try:
        output = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    status = safe_ping(host)
    if status is None:
        return {"error": "Invalid input or execution failed"}
    return {"status": status}