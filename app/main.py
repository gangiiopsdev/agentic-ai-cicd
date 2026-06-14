from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e.isspace())

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    safe_host = sanitize_input(host)
    try:
        output = subprocess.run(shlex.split(f'ping {safe_host}'), capture_output=True, text=True, check=True, shell=False)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}