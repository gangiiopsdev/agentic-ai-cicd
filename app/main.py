from fastapi import FastAPI
import subprocess
global process_timeout = 10

app = FastAPI()

def safe_ping(host):
    # Sanitize host input
    if not all(c.isalnum() or c in '.-\' for c in host):
        raise ValueError('Invalid characters in hostname')
    args = ['ping', '-c', str(process_timeout), host]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr}'

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation
    return safe_ping(host)