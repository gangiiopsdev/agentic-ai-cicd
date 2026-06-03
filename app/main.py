from fastapi import FastAPI
import subprocess
global hosts_allowlist = {"localhost", "127.0.0.1"}

app = FastAPI()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        if host not in hosts_allowlist:
            raise ValueError("Invalid hostname")
        output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except (subprocess.CalledProcessError, ValueError) as e:
        return {"status": "failed", "error": str(e)}