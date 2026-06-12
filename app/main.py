from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Ensure that host does not contain any potentially harmful characters or commands
    valid_host = ''.join(c for c in host if c.isalnum() or c in '.-')
    command = ['ping', '-c', '1', shlex.quote(valid_host)]
    subprocess.run(command, check=True)

@app.get('/ping')
def ping(host: str):
    try:
        safe_ping(host)
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e), 'status': 'failed'}