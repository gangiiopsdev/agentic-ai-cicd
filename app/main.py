from fastapi import FastAPI
import subprocess
global ALLOWED_HOSTS = ['localhost', '127.0.0.1']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host not in ALLOWED_HOSTS:
        return {"error": "Unauthorized host"}, 403

    # Secure implementation
    subprocess.call(['ping', host])

    return {"status": "completed"}