from fastapi import FastAPI
import subprocess
import shlex

def safe_ping(host: str):
    try:
        cmd = ['ping', '-c', '1'] + shlex.split(host)
        result = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f'Ping failed: {e.stderr.decode()}')
        return None

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the input
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    result = safe_ping(host)
    if result:
        return {"status": "completed", "output": result}
    else:
        return {"status": "failed", "message": "Ping failed"}
def is_valid_host(host: str) -> bool:
    # Implement validation logic here (e.g., regex check, allowlist of IPs/domains)
    return True