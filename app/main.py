from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(value):
    return ''.join(e for e in value if e.isalnum() or e.isspace())

@app.get('/ping')
def ping(host: str):
    try:
        sanitized_host = sanitize_input(host)
        if not sanitized_host.strip():
            raise ValueError('Invalid host provided')
        args = shlex.split(f'ping {sanitized_host}')
        subprocess.check_output(args, stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    except ValueError as ve:
        return {'status': 'failed', 'error': str(ve)}