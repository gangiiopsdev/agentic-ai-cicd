from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: f'ping {host}' if isinstance(host, str) and all(c.isalnum() or c in ('.', '-', '_') for c in host) else 'ping example.com'
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    # Secure implementation
    command = generate_ping_command(host)
    subprocess.call(command, shell=False)
    return {"status": "completed"}