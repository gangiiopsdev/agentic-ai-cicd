from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        # Use subprocess.run instead of subprocess.call for better control and security
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    # Call the safe_ping function instead of using subprocess.call
    status = safe_ping(host)
    return {"status": "completed", "output": status}