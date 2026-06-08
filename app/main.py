from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    return ''.join(filter(str.isalnum, input_str))

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host:
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        output = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
        return {'status': 'completed', 'output': output.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}