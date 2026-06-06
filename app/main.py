from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    return ''.join(char for char in input_str if char.isalnum() or char in '.:/-')
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    # Sanitize the host input to prevent command injection
    sanitized_host = sanitize_input(host)
    if not sanitized_host.strip():
        return {'status': 'error', 'message': 'Invalid host'}
    try:
        result = subprocess.run(['ping', '-c', '4'] + shlex.split(sanitized_host), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}