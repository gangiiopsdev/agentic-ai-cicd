from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    if not input_str.isnumeric() and '-' not in input_str and '/' not in input_str:
        return True
    return False

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if sanitize_input(host):
        command_parts = ['ping', shlex.quote(host)]
        try:
            output = subprocess.run(command_parts, capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': output.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}
    else:
        return {'status': 'invalid_host', 'message': 'Invalid host provided'}