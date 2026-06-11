from fastapi import FastAPI
import subprocess
from shlex import quote
def sanitize_input(input_string):
    return ''.join(filter(str.isalnum, input_string))

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    host = sanitize_input(host)
    result = subprocess.run(['ping', quote(host)], capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}