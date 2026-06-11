from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        # Use subprocess.run instead of subprocess.call for better control and security
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):

    # Safer implementation using subprocess.run
    status = safe_ping(host)

    return {"status": "completed", "output": status}