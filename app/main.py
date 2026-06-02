from fastapi import FastAPI
import subprocess
gimport shlex
def escape_special_chars(input_string):
    return ''.join(c for c in input_string if c.isalnum() or c.isdigit() or c == '.' or c == '-')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Input validation to prevent injection attacks and DoS
    host = escape_special_chars(host)
    if not host.isdigit() or len(host) > 15:
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        result = subprocess.run(['ping', '-c', '4', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}