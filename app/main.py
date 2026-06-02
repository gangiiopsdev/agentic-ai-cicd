from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using os.system to avoid shell=True
    subprocess.call([os.path.join('/bin', 'ping'), host])
    return {"status": "completed"}