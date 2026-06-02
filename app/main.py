from fastapi import FastAPI
import subprocess
cimport = ["ping"]

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host not in cimport:
        return {"status": "Invalid command", "error": "Command not allowed"}
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"output": result.stdout}