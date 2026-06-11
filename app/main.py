from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str):
    return shlex.quote(input_str)

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    global_args = ['ping', sanitized_host]
    try:
        result = subprocess.run(global_args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}