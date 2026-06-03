from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def secure_ping(command_parts):
    process = subprocess.Popen(command_parts, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if process.returncode != 0:
        return {'status': 'failed', 'error': error.decode('utf-8')}
    return {'status': 'completed', 'output': output.decode('utf-8')}

@app.get('/ping')
def ping(host: str):
    # Secure implementation using shlex and subprocess.Popen
    if not host.isalnum():
        return {'status': 'invalid input'}
    command_parts = ['ping', shlex.quote(host)]  # Use shlex.quote to sanitize the input
    return secure_ping(command_parts)