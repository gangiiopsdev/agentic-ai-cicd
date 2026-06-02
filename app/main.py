from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    return ''.join(c for c in input_str if c.isdigit())
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    try:
        # Sanitize input by ensuring it only contains digits
        sanitized_host = sanitize_input(host)
        result = subprocess.run(['ping', '-c', str(sanitized_host)], check=True, stdout=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}