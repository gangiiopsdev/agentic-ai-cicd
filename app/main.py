from fastapi import FastAPI
import subprocess
def validate_host(host):
    if host.strip() == 'localhost' or host.startswith('192.168.'):  # Example of basic validation
        return True
    else:
        return False

app = FastAPI()

@app.get('/ping')
def ping(host: str):    # Validate the input to avoid command injection
    if validate_host(host):
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'status': 'error', 'message': 'Invalid host'}, 400