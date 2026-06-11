from fastapi import FastAPI
import subprocess

def validate_host(host):
    allowed_hosts = ['host1', 'host2']
    if host in allowed_hosts:
        return True
    return False

generate_safe_command = lambda host: ['ping', host]

app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        # Secure implementation using subprocess.run with shell=False and proper argument handling
        subprocess.run(generate_safe_command(host), check=True)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}, 400