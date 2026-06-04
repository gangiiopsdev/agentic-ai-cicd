from fastapi import FastAPI
import subprocess

generate_ping_command = lambda host: f"ping {host}"

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it does not contain malicious content
    if not host.isalnum():
        return {"error": "Invalid hostname"}, 400
    try:
        subprocess.run(generate_ping_command(host).split(), check=True)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}, 500