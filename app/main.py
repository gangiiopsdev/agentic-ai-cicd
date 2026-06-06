from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host parameter to ensure it does not contain malicious characters
    if any(char in host for char in [';', '&', '|', '<', '>', '\', '$', '`']):
        return {"status": "failed", "error": "Invalid input"}
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}