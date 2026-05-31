from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str):
    return shlex.quote(input_str)

@app.get('/ping')
def ping(host: str):
    try:
        # Sanitize input by ensuring it only contains digits
        if host.strip().isdigit():
            sanitized_host = sanitize_input(host)
            result = subprocess.run(['ping', '-c', '4', sanitized_host], check=True, stdout=subprocess.PIPE)
            return {'status': 'completed', 'output': result.stdout.decode()}
        else:
            return {'status': 'failed', 'error': 'Invalid input'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}