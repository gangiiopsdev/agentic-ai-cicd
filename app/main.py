from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: f'ping {host}'

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize the host input to prevent command injection
    safe_host = ''.join(e for e in host if e.isalnum() or e in ['-', '.', '_', ' ', ':'])
    # Use subprocess.run with shell=False to avoid potential risks
    result = subprocess.run(['ping', '-c', '1', safe_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}