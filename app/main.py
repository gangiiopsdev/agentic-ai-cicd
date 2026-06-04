from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    try:
        # Validate and sanitize the host input
        if not host.isalnum() or len(host) > 255:
            raise ValueError('Invalid host')
        args = ['ping', '-c', '1'] + [shlex.quote(arg) for arg in shlex.split(host)]
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get("/ping")
def ping_route(host: str):
    return ping(host)