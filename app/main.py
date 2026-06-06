from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input):
    return ''.join(filter(str.isalnum, input))

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Safe implementation
    try:
        output = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}