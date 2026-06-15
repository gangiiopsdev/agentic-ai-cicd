from fastapi import FastAPI
import subprocess
def run_ping(host):
    if host and host.isnumeric():
        return subprocess.run(['/usr/bin/ping', str(host)], capture_output=True, text=True, check=True)
    else:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        result = run_ping(host)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': f'Ping failed with error: {e.stderr}'}
    except ValueError as e:
        return {'error': str(e)}