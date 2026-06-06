from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        # Use subprocess.run instead of subprocess.call for safer execution
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    response = safe_ping(host)
    return {"status": "completed", "response": response}