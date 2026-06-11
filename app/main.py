from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        print(f'Ping failed: {e.stderr.decode()}')
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the input
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    safe_ping(host)
    return {"status": "completed"}
def is_valid_host(host: str) -> bool:
    # Implement validation logic here (e.g., regex check, allowlist of IPs/domains)
    return True