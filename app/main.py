from fastapi import FastAPI
import subprocess
import re
import shlex

app = FastAPI()

def validate_host(host):
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None

def sanitize_input(input_string):
    return ''.join(filter(str.isalnum, input_string))

@app.get('/ping')
def ping(host: str):
    if validate_host(sanitize_input(host)):
        try:
            command = ['ping', shlex.quote(host)]
            output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
            return {'status': 'completed', 'output': output}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output}
    else:
        return {'status': 'failed', 'error': 'Invalid host'}