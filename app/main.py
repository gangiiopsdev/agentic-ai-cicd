from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize input
    if host.strip() != host or ' ' in host:
        return {'error': 'Invalid host input'}

    command = ['ping', shlex.quote(host)]
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        return {'error': 'Ping failed', 'details': str(e)}

    return {'status': 'completed'}