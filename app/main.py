from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with proper validation
    if not host or len(host) > 100 or any(char in ' 	
' for char in host):
        return {"status": "invalid_host"}
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {
        "status": "completed",
        "output": result.stdout,
        "stderr": result.stderr
    }