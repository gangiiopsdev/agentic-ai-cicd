from fastapi import FastAPI
import re
def safe_ping(host):
    # Validate and sanitize the host input
    regex = re.compile(r'^[a-zA-Z0-9.-]+$')
    if not regex.match(host):
        raise ValueError('Invalid host format')
    cmd = ['ping', '-c', '1', host]
    result = subprocess.run(cmd, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)