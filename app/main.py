from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    # Sanitize user input
    if not all(c.isalnum() or c in ('.', '-') for c in host):
        return {'status': 'error', 'message': 'Invalid input'}
    output = safe_ping(host)
    return {'status': 'completed', 'output': output}