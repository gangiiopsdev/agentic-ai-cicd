from fastapi import FastAPI
import subprocess
import shlex
def escape_host(host):
    return ''.join(char if char.isalnum() or char in ('.', '-', '_') else '_' for char in host)
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    escaped_host = escape_host(host)
    command = ['ping', escaped_host]
    result = subprocess.run(command, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}