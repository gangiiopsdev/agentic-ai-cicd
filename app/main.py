from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize input by checking for malicious patterns
    if any(char in host for char in [';', '&', '|', '<', '>', '`']):
        return {'status': 'error', 'message': 'Invalid characters in hostname'}

    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.output.decode()}
    except Exception as e:
        return {'status': 'error', 'error': str(e)}