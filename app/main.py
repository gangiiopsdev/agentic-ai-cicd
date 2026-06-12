from fastapi import FastAPI
import subprocess
def run_ping(host):
    try:
        # Use a safe and secure way to execute the ping command
        output = subprocess.check_output(['ping', host], universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return run_ping(host)