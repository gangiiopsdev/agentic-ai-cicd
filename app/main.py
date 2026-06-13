from fastapi import FastAPI
import subprocess
def run_safe_ping(host):
    try:
        # Use shell=False and ensure host does not contain any executable code
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

global app
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    output = run_safe_ping(host)
    return {"status": "completed", "output": output}