from fastapi import FastAPI
import subprocess
import shlex
import time

class InputSanitizer:
    @staticmethod
def sanitize_input(input_str):
        return ''.join(filter(str.isalnum, input_str))

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host or len(host) > 100:
        return {'status': 'error', 'message': 'Invalid input'}
    sanitized_host = InputSanitizer.sanitize_input(host)
    # Use shlex.quote to safely include the host in the command line
    result = subprocess.run(['ping', '-c', '1', shlex.quote(sanitized_host)], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}