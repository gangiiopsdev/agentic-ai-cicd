from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def escape_host(host):
    return ''.join(char if char.isalnum() or char in ('.', '-', '_') else '_' for char in host)

@app.get('/ping')
def ping(host: str):
    escaped_host = escape_host(host)
    command = ['ping', escaped_host]
    args = shlex.split(' '.join(command))
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}