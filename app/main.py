from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Use subprocess.run instead of subprocess.call and sanitize the host
        result = subprocess.run(['ping', subprocess.check_output(f'echo {host}', shell=True, text=True).strip()], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not all(c.isalnum() or c in ('.', '-') for c in host):
        return {'status': 'failed', 'error': 'Invalid characters in hostname'}
    return safe_ping(host)