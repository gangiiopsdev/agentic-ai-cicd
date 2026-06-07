from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
        return result.stdout
    except Exception as e:
        return f'Error: {e}'

@app.get("/ping")
def ping(host: str):
    # Safer implementation
    if not host.isalnum():  # Example validation check for simplicity
        return {'status': 'error', 'output': 'Invalid input'}
    output = safe_ping(host)
    return {'status': 'completed', 'output': output}