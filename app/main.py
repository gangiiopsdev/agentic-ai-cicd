from fastapi import FastAPI
import subprocess
def sanitize_host(host):
    return ''.join(e for e in host if e.isalnum() or e in '.-_')
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if not sanitized_host:
        return {'status': 'failed', 'error': 'Invalid hostname'}
    try:
        result = subprocess.run(['ping', '-c', '1', subprocess.check_output(f'echo {sanitized_host}').decode()], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}