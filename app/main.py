from fastapi import FastAPI
import subprocess
from shlex import quote as shell_quote
from fastapi import HTTPException

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e.isdigit())

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = ['ping', shell_quote(sanitized_host)]
    try:
        subprocess.run(args, check=True, capture_output=True, text=True, shell=False)
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f'Ping failed: {e}')
    return {'status': 'completed'}