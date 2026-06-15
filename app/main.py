from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: ["ping", host]

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation using subprocess.run instead of shell=True
    try:
        result = subprocess.run(generate_ping_command(host), capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        return {"status": "error", "output": e.stderr}
    return {"status": "completed", "output": result.stdout}