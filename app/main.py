from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

def sanitize_input(input_string):
    # Add your custom sanitization logic here
    return input_string.strip().lower()

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command = ['ping', shlex.quote(sanitized_host)]
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        return {'error': 'Ping failed', 'details': str(e)}

    return {'status': 'completed'}