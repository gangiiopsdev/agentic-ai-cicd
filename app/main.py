from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(c for c in input_str if c.isdigit())

@app.get('/ping')
def ping(host: str):
    try:
        host = sanitize_input(host.strip())
        if host.isdigit():
            result = subprocess.run(['ping', '-c', '4', host], check=True, stdout=subprocess.PIPE)
            return {'status': 'completed', 'output': result.stdout.decode()}
        else:
            return {'status': 'failed', 'error': 'Invalid input'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}