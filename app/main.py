from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_safe_ping(host):
    try:
        # Use subprocess.run instead of subprocess.call and avoid using shell=True
        result = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5)
        return result.stdout
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    # Safely run the ping command
    response = run_safe_ping(host)
    return {"status": "completed", "response": response}