from fastapi import FastAPI
import subprocess
from fastapi import HTTPException
import shlex

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(c if c.isalnum() or c in ['-', '.'] else '_' for c in input_str)

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = ['ping', '-c', '1'] + shlex.split(sanitized_host)  # Use shlex to handle the command safely
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'result': result.stdout}