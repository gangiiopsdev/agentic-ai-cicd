from fastapi import FastAPI
import subprocess
def execute_ping(host):
    return subprocess.call(['ping', host])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        return execute_ping(host)
    else:
        return {"error": "Invalid host"}, 400

def validate_host(host):
    # Add validation logic here, e.g., checking for allowed IP ranges or domains
    return True