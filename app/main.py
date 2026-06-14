from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the input to ensure it is a valid host name or IP address
    if not re.match(r'^([0-9]{1,3}\.[0-9]{1,3}\.){2}[0-9]{1,3}$', host) and not host.isalnum():
        raise ValueError("Invalid host")
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}