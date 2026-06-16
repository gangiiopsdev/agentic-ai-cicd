from fastapi import FastAPI
import subprocess
def validate_host(host):
    return host.isalnum() and '.' in host

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"error": "Invalid host input"}, 400

    args = ['ping', '--'] + [host]
    subprocess.run(args, check=True)

    return {"status": "completed"}