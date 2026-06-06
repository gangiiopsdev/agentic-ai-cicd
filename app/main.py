from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Safe implementation using subprocess.run with proper arguments and shell=False
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return result.stdout

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Sanitize input to prevent command injection
        safe_host = shlex.quote(host)
        output = subprocess.run(['ping', safe_host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}