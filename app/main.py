from fastapi import FastAPI
import subprocess
import re
import shlex

app = FastAPI()

def sanitize_input(input_string):
    return shlex.quote(input_string)

def execute_command(command_parts):
    try:
        result = subprocess.run(command_parts, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': e.stderr or str(e)}, 400

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not re.match(r'^[a-zA-Z0-9.-]+$', sanitized_host):
        return {'error': 'Invalid host input'}, 400
    command_parts = ['ping', sanitized_host]
    return execute_command(command_parts)