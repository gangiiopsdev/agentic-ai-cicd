from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    return ''.join(ch for ch in input_str if ch.isalnum() or ch in ('.', '-', '_'))

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        host = sanitize_input(host)
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}