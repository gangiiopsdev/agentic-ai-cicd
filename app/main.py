from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    allowed_hosts = ['example.com', 'another-example.com']  # Define a list of allowed hosts
    if host in allowed_hosts:
        args = shlex.split(f'ping {host}')
        output = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    else:
        raise ValueError('Host not allowed')

@app.get("/ping")
def ping(host: str):
    try:
        return safe_ping(host)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}