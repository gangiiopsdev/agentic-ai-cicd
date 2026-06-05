from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

def safe_ping(host: str):
    if not all(c.isalnum() or c in ('.', '-', '_') for c in host):
        raise ValueError('Invalid hostname')
    command = ['ping', '--'] + [shlex.quote(host)]  # Use -- to prevent options from being interpreted as positional arguments
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    try:
        output = safe_ping(host)
    except ValueError as e:
        return {'error': str(e)}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}
    return {'status': 'completed', 'output': output}