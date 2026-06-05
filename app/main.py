from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: f"ping {host}"

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Validate the host to ensure it's a valid IP address or hostname
        subprocess.call(generate_ping_command(host), shell=False)
        return {"status": "completed"}
    except Exception as e:
        return {"status": "failed", "error": str(e)}