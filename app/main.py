from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Sanitize input and use shlex for safe argument parsing
    host = host.strip().replace(' ', '_')
    if not shlex.quote(host) == host:
        return {'error': 'Invalid characters in host'}
    command = ['ping', shlex.quote(host)]
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        return {'error': f'Ping failed with error: {e}'}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)