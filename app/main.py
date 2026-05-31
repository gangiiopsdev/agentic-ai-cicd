from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the input to prevent command injection
    if not host.isalnum() or len(host) > 255:
        return {'status': 'error', 'output': 'Invalid input'}
    safe_host = shlex.quote(host)
    result = subprocess.run(['ping', '-c', '1'], capture_output=True, text=True, check=False)
    return {'status': 'completed', 'output': result.stdout}