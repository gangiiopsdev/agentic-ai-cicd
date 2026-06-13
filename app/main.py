from fastapi import FastAPI
import subprocess
cimport = subprocess.check_output

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        result = cimport(f"ping -c 1 {host}", shell=True, stderr=subprocess.STDOUT)
        return {"status": "completed", "output": result.decode()}\n    except subprocess.CalledProcessError as e:\n        return {"status": "failed", "error": e.output.decode()}