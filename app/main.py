from fastapi import FastAPI
import subprocess
import shlex
gimport shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation with input validation
    if host and host.strip() and host.count('.') == 3:
        args = shlex.split(f'ping -c 4 {host}')  # Limit the number of pings to prevent DoS
        try:
            result = subprocess.run(args, check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e), 'output': e.stderr}
    else:
        return {'status': 'failed', 'error': 'Invalid host'}
    return {'status': 'completed'}