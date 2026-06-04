from fastapi import FastAPI
import subprocess
def escape_command(command):
    return [arg.strip() for arg in command.split()]

def validate_host(host):
    # Add validation logic here to ensure 'host' is safe to use with ping
    allowed_hosts = ['example.com', 'localhost']  # Example list of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        validate_host(host)
        subprocess.call(escape_command(f'ping {host}'), shell=False)
    except Exception as e:
        return {"error": str(e)}
    return {"status": "completed"}