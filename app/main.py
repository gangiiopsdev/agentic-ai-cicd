from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    if not host or len(host) > 255:
        return {'status': 'failed', 'error': 'Invalid host name'}
    try:
        # Use a full path for the executable to mitigate risks
        result = subprocess.run(['/usr/bin/ping', shlex.quote(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)