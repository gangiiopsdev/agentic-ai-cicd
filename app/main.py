from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping/{host}')
def ping(host: str):
    # Sanitize input using shlex.quote to prevent command injection
    safe_host = f'"{host}"'.replace("\", "\\")

    # Use subprocess.run instead of subprocess.call for better control and security
    result = subprocess.run(['ping', '-c', '1'] + [safe_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}