from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_input(input_string):
    return ''.join(c for c in input_string if c.isalnum() or c in '._-')

@app.get('/ping')
def ping(host: str):
    safe_host = escape_input(host)
    try:
        output = subprocess.run(['ping', safe_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}