from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation
    if not validate_host(host):
        raise ValueError('Invalid host')
    args = ['ping', host]
    try:
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE)
        return {'host': host, 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'host': host, 'error': e.stderr.decode()}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)

def validate_host(host: str) -> bool:
    # Add validation logic here
    return all(c.isalnum() or c in ('.', '-') for c in host)