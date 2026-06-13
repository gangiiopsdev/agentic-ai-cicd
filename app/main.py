from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: ["ping", host]

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    if not host.isalnum() or len(host) > 255:
        return {"status": "error", "message": "Invalid host name"}

    # Use subprocess.run instead of subprocess.call for better control and security
    result = subprocess.run(generate_ping_command(host), capture_output=True, text=True, check=False)
    if result.returncode != 0:
        return {"status": "error", "message": "Ping command failed: " + result.stderr}
    return {"status": "completed", "output": result.stdout}