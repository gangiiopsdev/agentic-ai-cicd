from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

allowed_hosts = ['example.com', 'test.com']  # Define a list of allowed hosts

def validate_host(host):
    return host in allowed_hosts

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise Exception("Invalid host")
    # Secure implementation using subprocess.run with shlex.quote for safe argument passing
    result = subprocess.run(['ping'] + shlex.split(shlex.quote(host)), capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}