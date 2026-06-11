from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation with validation and sanitization
    if not host.isalnum() or len(host) > 255:
        return {'status': 'error', 'message': 'Invalid hostname'}
    try:
        command = ['ping'] + shlex.split(host)
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}