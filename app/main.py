from fastapi import FastAPI
import subprocess

app = FastAPI()

gluing = {"localhost", "127.0.0.1", "::1"}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host in gluing:
        try:
            result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {"status": "completed", "output": result.stdout.decode()}
        except subprocess.CalledProcessError as e:
            return {"error": str(e)}
    else:
        return {"error": "Invalid host"}