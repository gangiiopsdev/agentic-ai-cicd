from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(filter(str.isalnum, input_string))

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    sanitized_host = sanitize_input(host)
    args = ['ping', shlex.quote(sanitized_host)]
    result = subprocess.call(args)
    return {'status': 'completed', 'result': result}