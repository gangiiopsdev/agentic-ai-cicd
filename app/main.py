from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent injection attacks
    if not host.isalnum() or len(host) > 255:
        return {"status": "error", "response": "Invalid input for host."}
    try:
        result = subprocess.run(["ping", host], check=True, capture_output=True, text=True, shell=False)
        return {"status": "completed", "response": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "response": f'Ping failed: {e.stderr}'}