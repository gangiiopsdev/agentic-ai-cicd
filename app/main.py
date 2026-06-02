from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation using list of arguments
    args = ['ping', host]
    subprocess.run(args, check=True)
app = FastAPI()
@app.get("/ping")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/secure-ping")
def secure_ping(host: str):
    # Secure implementation using list of arguments
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}