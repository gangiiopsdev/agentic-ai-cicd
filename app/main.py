from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host: str) -> bool:
    allowed_hosts = ('192.168.', '172.16.', '10.')
    return any(host.startswith(allowed) for allowed in allowed_hosts) or host == 'localhost'

@app.get("/ping")
def ping(host: str):
    if sanitize_host(host):
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    else:
        return {'status': 'failed', 'error': 'Invalid host'}