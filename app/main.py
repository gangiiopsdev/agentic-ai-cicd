from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Secure implementation using subprocess.run with shell=False and executable specified
        result = subprocess.run(['/bin/ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    # Validate input to ensure it does not contain malicious content
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    return ping(host)