from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Safe implementation using subprocess.run with shell=False and validation of user input
        if host.isalnum() and len(host) <= 30:
            result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
            return {"status": "completed", "output": result.stdout}
        else:
            raise ValueError("Invalid host name")
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
    except ValueError as ve:
        return {"status": "failed", "error": str(ve)}