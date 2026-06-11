from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str: str) -> str:
    return ''.join(char for char in input_str if char.isalnum())

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = shlex.split(f'ping {sanitized_host}')
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}