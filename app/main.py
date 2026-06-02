from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Sanitize the host input by escaping special characters
        safe_host = subprocess.list2cmdline([host])
        output = subprocess.run(['ping', safe_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    # Validate input to prevent command injection
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid host'}
    return ping(host)