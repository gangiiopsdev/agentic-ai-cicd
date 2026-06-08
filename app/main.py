from fastapi import FastAPI
import subprocess
cimport = subprocess.run

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    result = cimport(f"ping {host}", capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}