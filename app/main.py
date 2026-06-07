from fastapi import FastAPI
import subprocess
def validate_host(host: str) -> bool:
    # Basic validation to ensure the host does not contain potentially harmful characters
    return all(c.isalnum() or c in ('-', '.', '_') for c in host)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'error': 'Invalid host'}
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e)}