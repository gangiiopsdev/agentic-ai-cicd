from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        if not host.startswith('192.168.') or ' ' in host:  # Example IP filter and whitespace check
            raise ValueError("Invalid host")
        subprocess.run(["ping", host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}