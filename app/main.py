from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    # Add input sanitization logic here
    return ''.join(e for e in input_str if e.isalnum() or e.isspace())

app = FastAPI()

@app.get('/ping')
def ping(host: str):    host = sanitize_input(host)
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}