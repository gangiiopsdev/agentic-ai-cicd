from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        # Use f-string to safely include host in the command
        result = subprocess.run(['ping', host], check=True, timeout=5, capture_output=True)
        return {
            "status": "completed",
            "result": result.stdout.decode('utf-8')
        }
    except Exception as e:
        return {"status": "failed", "error": str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)