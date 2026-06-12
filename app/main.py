from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: ['ping', host]

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not is_valid_host(host):
        return {"error": "Invalid host"}, 400
    subprocess.run(generate_ping_command(host), check=True)
    return {"status": "completed"}

def is_valid_host(host):
    allowed_hosts = ['google.com', 'github.com']  # Example list of allowed hosts
    return host in allowed_hosts