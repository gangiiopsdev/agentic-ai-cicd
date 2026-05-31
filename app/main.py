from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

@app.get('/ping')
def ping_endpoint(host: str):
    # Validate the host input to ensure it does not contain malicious content
    if any(char in host for char in [';', '&', '|', '>', '<', '`', '$', '*', '?', '{', '}', '[', ']', '\', '^', '~', '%', '#']):
        return {'status': 'error', 'message': 'Invalid input'}
    return ping(host)