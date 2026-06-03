from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate the host input to ensure it does not contain malicious content
    if not host.isalnum() or '.' not in host:
        return {"status": "failed", "error": "Invalid host format"}

    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)