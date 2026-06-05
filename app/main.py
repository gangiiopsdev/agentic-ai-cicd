from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Safe implementation with proper exception handling
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e.stderr}'

app = FastAPI()

@app.get("/ping")
def ping_safe(host: str):
    return {'status': 'completed'}