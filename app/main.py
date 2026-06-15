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
    if not all(c.isalnum() or c in ['.', '-', '_'] for c in host):
        return {"error": "Invalid hostname"}, 400
    subprocess.call(generate_ping_command(host))
    return {"status": "completed"}