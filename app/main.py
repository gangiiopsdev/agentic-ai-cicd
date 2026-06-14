from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input):
    return ''.join(filter(str.isalnum, input))
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        result = subprocess.run(['ping', '-c', '1', shlex.quote(sanitized_host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/ping/{host}')
def read_ping(host: str):
    return ping(host)