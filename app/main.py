from fastapi import FastAPI
import subprocess
getpass = __import__("getpass")

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with input validation
    if validate_host(host):
        subprocess.call(['ping', host])
    else:
        raise ValueError("Invalid host")
    
    return {"status": "completed"}

def validate_host(host: str) -> bool:
    allowed_hosts = ['example.com', 'localhost']  # Define a list of allowed hosts
    return host in allowed_hosts