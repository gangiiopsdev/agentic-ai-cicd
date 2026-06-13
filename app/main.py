from fastapi import FastAPI
import subprocess
import shlex
generate_ping_command = lambda host: ["ping", shlex.quote(host)]

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not all(char.isalnum() or char in '.-' for char in host):
        return {"status": "failed", "error": "Invalid input"}
    try:
        result = subprocess.run(generate_ping_command(host), capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}