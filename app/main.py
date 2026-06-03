from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent injection attacks
    if not host.isalnum() or ' ' in host:
        return {"status": "failed", "error": "Invalid host"}
    try:
        output = subprocess.run([f'ping', '-c', '1', subprocess.check_output(f'echo {host}', shell=True).decode('utf-8').strip()], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}