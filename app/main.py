from fastapi import FastAPI
import subprocess
def run_ping(host: str):
    try:
        # Use a safe and sanitized way to construct the command
        cmd = ['ping', host]
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f'Ping failed with error: {e})
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = run_ping(host)
    if result:
        return {"status": "completed", "output": result}
    else:
        return {"status": "failed"}