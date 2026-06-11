from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not host.strip() or len(host) > 255:
        return {"status": "failed", "error": "Invalid host"}
    try:
        output = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}