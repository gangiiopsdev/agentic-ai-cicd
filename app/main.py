from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    allowed_hosts = ['localhost', '127.0.0.1']
    if host in allowed_hosts:
        try:
            command = shlex.split('ping -c 4 {}'.format(host))
            result = subprocess.run(command, capture_output=True, text=True, check=True, shell=False)
            return result.stdout
        except subprocess.CalledProcessError as e:
            raise ValueError(f'Ping failed: {e}')
    else:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    output = safe_ping(host)
    return {'status': 'completed', 'output': output}