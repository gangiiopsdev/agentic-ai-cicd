from fastapi import FastAPI
import subprocess
import shlex
import re
def sanitize_input(input_str):
    # Implement input sanitization logic here
    return ''.join(c for c in input_str if c.isalnum() or c in ['.', ':', '-'])

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    host = sanitize_input(host)
    args = ['ping'] + shlex.split(re.escape(host))
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}