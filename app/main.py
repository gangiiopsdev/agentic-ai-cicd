from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def _sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() and e.isprintable())

@app.get('/ping')
def ping(host: str):
    sanitized_host = _sanitize_input(host)
    result = subprocess.run(['ping', shlex.quote(sanitized_host)], capture_output=True, text=True, check=False)
    if result.returncode != 0:
        return {'status': 'failed', 'error': result.stderr}
    return {'status': 'completed', 'output': result.stdout}