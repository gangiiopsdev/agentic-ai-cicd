from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_string):
    if not input_string.isalnum():
        raise ValueError('Invalid input')
    return input_string

@app.get('/ping')
def ping(host: str):
    try:
        sanitized_host = sanitize_input(host)
        command = ['ping', *shlex.split(sanitized_host)]
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    except ValueError as ve:
        return {'status': 'failed', 'error': str(ve)}