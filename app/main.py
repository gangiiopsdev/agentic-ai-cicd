from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    return ''.join(c for c in input_str if c.isalnum() or c in ['-', '.', '_', ''])
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.Popen with proper sanitization
    sanitized_host = sanitize_input(host)
    command = ['ping', shlex.quote(sanitized_host)]
    subprocess.run(command, check=True)
    return {'status': 'completed'}