from fastapi import FastAPI
import subprocess

generate_ping_command = lambda host: ["ping", host]

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the input to prevent command injection
    if not host.isalnum() or len(host) > 255:
        return {"error": "Invalid host parameter"}, 400
    subprocess.call(generate_ping_command(host), shell=False)
    return {"status": "completed"}