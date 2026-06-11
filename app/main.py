from fastapi import FastAPI
import subprocess
import shlex
def escape_host(host: str):
    return shlex.quote(host)

def validate_host(host: str):
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError("Invalid host")

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        validated_host = validate_host(host)
        escaped_host = escape_host(validated_host)
        command = f'ping {escaped_host}'
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return {'output': result.stdout}
    except Exception as e:
        return {'error': str(e)}