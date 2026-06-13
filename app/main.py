from fastapi import FastAPI
import subprocess
import shlex
class SanitizeError(Exception):
    pass
def sanitize_input(input_string):
    if not input_string.isalnum():
        raise SanitizeError('Invalid input')
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    try:
        sanitized_host = shlex.quote(host)
        result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}
    except SanitizeError as se:
        return {'status': 'invalid_input', 'error': se.args[0]}