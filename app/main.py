from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    if not valid_host(host):
        raise ValueError("Invalid host")
    result = safe_ping(host)
    return {"status": "completed", "result": result}

# Preventive control to validate the host input
def valid_host(host):
    # Add logic to validate the host, e.g., checking for allowed domains or IP ranges
    return True