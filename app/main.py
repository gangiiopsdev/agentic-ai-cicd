from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the input before using it in the command
    import re
    if not re.match(r'^[a-zA-Z0-9-.]+$', host):
        raise ValueError('Invalid hostname')
    return {'status': 'completed', 'output': safe_ping(host)}