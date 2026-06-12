from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping/{host}')
def ping(host: str):
    # Sanitize input using shlex.quote to prevent command injection
    safe_host = shlex.quote(host)

    # Use subprocess.run instead of subprocess.call for better control and security
    result = subprocess.run(['ping', '-c', '1'] + [safe_host], capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}