from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    # Basic sanitization logic to avoid command injection
    return ''.join(c for c in input_string if c.isalnum() or c in '.-')

cmd = ['ping', sanitize_input(host)]

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}