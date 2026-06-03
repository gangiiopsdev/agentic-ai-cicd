from fastapi import FastAPI
import shlex
def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e.isdigit())
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not is_valid_host(sanitized_host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        result = subprocess.run(shlex.split(f'ping {sanitized_host}'), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}