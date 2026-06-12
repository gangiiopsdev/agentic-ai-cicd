from fastapi import FastAPI
import subprocess
def sanitize_host(host):
    if not all(c.isalnum() or c in '.-' for c in host):
        raise ValueError("Invalid host")
    return 'ping', host.strip()

cmd = ['ping']

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    command, sanitized_host = sanitize_host(host)
    cmd.append(sanitized_host)
    result = subprocess.run(cmd, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}