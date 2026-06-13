from fastapi import FastAPI
import subprocess

def safe_ping(host):
    # Use subprocess.run instead of subprocess.call and avoid shell=True for security reasons
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Call the safe version of ping function
    try:
        status = safe_ping(host)
    except subprocess.CalledProcessError as e:
        return {"status": "error", "output": str(e)}
    return {"status": "completed", "output": status}