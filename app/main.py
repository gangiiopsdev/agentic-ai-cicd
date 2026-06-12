from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input to avoid injection attacks
    safe_host = ''.join(c for c in host if c.isalnum() or c in '.-')
    output = safe_ping(safe_host)
    return {'status': 'completed', 'output': output}