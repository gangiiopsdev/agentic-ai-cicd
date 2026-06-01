from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Sanitize input to prevent injection attacks
        if not host.replace('.', '').replace('-', '').isdigit() and '-' not in host:
            raise ValueError('Invalid hostname')
        output = subprocess.check_output(['ping'] + shlex.split(host), stderr=subprocess.STDOUT, shell=False)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}
    except ValueError as ve:
        return {'status': 'failed', 'error': str(ve)}