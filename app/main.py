from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(c for c in input_str if c.isalnum() or c in '._-')

@app.get('/ping')
def ping(host: str):
    safe_host = sanitize_input(host)
    try:
        output = subprocess.run(shlex.split(f'ping -c 1 {safe_host}'), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}