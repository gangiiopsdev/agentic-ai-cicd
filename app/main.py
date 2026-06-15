from fastapi import FastAPI
import subprocess
import shlex
def safe_subprocess(command):
    if not all(c.isalnum() or c in [' ', '-'] for c in ' '.join(command)):
        raise ValueError('Invalid characters in command')
    return subprocess.run(shlex.join(command), shell=False)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isalnum():
        return {'error': 'Invalid input'}
    sanitized_host = ''.join(filter(str.isalnum, host))
    command = ['ping', sanitized_host]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}
    except ValueError as e:
        return {'error': str(e)}