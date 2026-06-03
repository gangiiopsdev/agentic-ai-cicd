from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str):
    if not input_str.isalnum() or len(input_str) > 255:
        raise ValueError('Invalid input')
    return input_str

@app.get('/ping')
def ping(host: str):
    host = sanitize_input(host)
    try:
        result = subprocess.run(['ping', '-c', '1', shlex.quote(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}