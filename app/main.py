from fastapi import FastAPI
import subprocess
import shlex
def sanitize_host(host):
    if not host.isalnum() or '-' not in host:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        sanitized_host = sanitize_host(host)
        args = ['ping', '-c', '1', shlex.quote(sanitized_host)]  # Use -c to limit the number of pings
        result = subprocess.run(args, capture_output=True, text=True, check=True)  # Use check=True to raise an exception on non-zero exit codes
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}
    except ValueError as e:
        return {'status': 'error', 'output': str(e)}