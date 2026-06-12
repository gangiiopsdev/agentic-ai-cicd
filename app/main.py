from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    try:
        # Validate and sanitize the host input
        if not is_valid_host(host):
            raise ValueError('Invalid host')
        args = ['ping', shlex.quote(host)]
        result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
def is_valid_host(host: str) -> bool:
    # Implement host validation logic here
    return '.' in host and not any(c.isnumeric() for c in host)
app = FastAPI()
@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)