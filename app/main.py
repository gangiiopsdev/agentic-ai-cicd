from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation using subprocess.Popen with proper argument passing
    subprocess.call(['ping', host])

app = FastAPI()

@app.get("/ping")
def ping_host(host: str):
    return ping(host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}