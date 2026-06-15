from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    try:
        # Use a safe method to avoid command injection
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}