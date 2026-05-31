from fastapi import FastAPI
import subprocess
import shlex
def escape_shell(s):
    return ''.join(c if c.isalnum() or c in '_-./:' else '_' for c in s)

def safe_ping(host: str):
    allowed_hosts = ['example.com', 'localhost']  # Define a whitelist of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')
    return subprocess.run(['ping', '-c', str(shlex.quote(host))], capture_output=True, text=True, check=True)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    result = safe_ping(host)
    return {'status': 'completed', 'output': result.stdout}