from fastapi import FastAPI
import subprocess
def sanitize_input(value):
    # Example implementation using regex for basic sanitization
    import re
    return re.sub(r'[^a-zA-Z0-9.-]', '', value)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        output = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}