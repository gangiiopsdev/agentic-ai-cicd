from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and splitting command into args
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {
            "status": "completed",
            "output": result.stdout,
            "stderr": result.stderr
        }
    except subprocess.CalledProcessError as e:
        return {
            "status": "failed",
            "error": str(e)
        }

def home():
    return {"message": "Agentic Self-Healing Pipeline"}

app.add_route("/ping", ping, methods=["GET"])