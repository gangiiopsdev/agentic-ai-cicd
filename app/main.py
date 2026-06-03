from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run instead of subprocess.call
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    try:
        output = safe_ping(host)
        return {'status': 'completed', 'output': output}
    except Exception as e:
        return {'status': 'error', 'error': str(e)}