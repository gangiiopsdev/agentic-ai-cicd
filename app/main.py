from fastapi import FastAPI
import subprocess
from shlex import quote
def escape_input(input_str):
    return input_str.replace(';', '').replace('&', '')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Using subprocess.run instead of subprocess.call for better security
        result = subprocess.run(['ping', '-c 1', quote(escape_input(host))], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}