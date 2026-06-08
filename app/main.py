from fastapi import FastAPI
import subprocess
import shlex
def execute_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e.stderr}'

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent command injection
    if not host.isalnum():
        return {'status': 'error', 'output': 'Invalid host'}
    escaped_host = shlex.quote(host)  # Escape special characters in the host
    command = ['ping', '-c', '1', escaped_host]  # Limit ping count to prevent flooding
    output = execute_command(command)
    return {'status': 'completed', 'output': output}