from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Validate input to ensure it's a valid hostname or IP address
    import re
    if re.match(r'^[a-zA-Z0-9.-]+$', host) is None:
        raise ValueError('Invalid hostname or IP address')
    command = ['ping', shlex.quote(host)]
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

@app.get('/ping')
def ping(host: str):
    result = safe_ping(host)
    if isinstance(result, dict) and 'error' in result:
        return result
    else:
        return {'status': 'completed'}