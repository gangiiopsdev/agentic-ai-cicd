from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    try:
        cmd = ['ping', host]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e}'

@app.get("/ping")
def ping(host: str):
    # Validate input
    if not host.strip() or '<' in host or '>' in host or ';' in host or '|' in host or '&' in host or '$' in host:
        return {'status': 'error', 'response': 'Invalid host input'}
    response = safe_ping(host)
    return {'status': 'completed', 'response': response}