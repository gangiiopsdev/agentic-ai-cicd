from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Enhanced validation to prevent injection attacks
    if not re.match(r'^[a-zA-Z0-9.-]{1,255}$', host):  # Adjusted regex for broader input validation
        return {'status': 'error', 'error': 'Invalid hostname'}
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, timeout=5, shell=False)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}
    except Exception as e:
        return {'status': 'error', 'error': str(e)}