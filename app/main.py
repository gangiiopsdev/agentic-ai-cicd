from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Validate host to prevent injection
        if not host.isalnum() or '.' not in host:
            raise ValueError("Invalid host format")
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except (subprocess.CalledProcessError, ValueError) as e:
        return {"status": "error", "output": str(e)}