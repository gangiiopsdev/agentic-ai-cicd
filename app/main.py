from fastapi import FastAPI
import subprocess
from html import escape

def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e.isdigit() or e.isspace())

app = FastAPI()
@app.get('/ping')
def ping(host: str):
    sanitized_host = escape(host)
    args = shlex.split(f'ping -c 1 {sanitized_host}')  # Limit the number of pings for security
    try:
        subprocess.run(args, check=True, shell=False, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e.stderr)}
    return {'status': 'completed'}