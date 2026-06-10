from fastapi import FastAPI
import subprocess
def sanitize_input(user_input):
    return ''.join(filter(str.isalnum, user_input))

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it is safe for use in a subprocess
    if not all(c.isalnum() or c in ['.', '-', '_'] for c in host):
        return {"status": "error", "message": "Invalid input"}
    result = subprocess.run(["/usr/bin/ping", "-c", "1", host], capture_output=True, text=True, check=False)
    if result.returncode != 0:
        return {"status": "error", "message": "Ping failed"}
    return {"status": "completed", "output": result.stdout}