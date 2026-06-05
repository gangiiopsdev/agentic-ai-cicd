from fastapi import FastAPI
import subprocess
import shlex

def safe_ping(host: str):
    try:
        # Use shlex to safely quote arguments
        command = ['ping', host]
        quoted_command = [shlex.quote(arg) for arg in command]
        result = subprocess.run(quoted_command, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate input to ensure it's safe to ping
    if not host.isalnum():
        raise ValueError('Invalid host name')
    return safe_ping(host)