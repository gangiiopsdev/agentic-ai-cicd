from fastapi import FastAPI
import subprocess

def ping(host: str):
    # Sanitize the host input to avoid injection attacks
    safe_host = subprocess.quote(host)
    try:
        # Safe implementation with timeout and error handling
        result = subprocess.check_output(['ping', safe_host], stderr=subprocess.STDOUT, timeout=5)
        return {
            "status": "completed",
            "result": result.decode('utf-8')
        }
    except subprocess.CalledProcessError as e:
        return {
            "status": "failed",
            "error": str(e)
        }

app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    return ping(host)