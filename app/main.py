from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse
from shlex import quote as cmd_quote

app = FastAPI()

def safe_ping(host):
    if not host:
        return None
    try:
        # Validate the command input
        if not host.isalnum():
            raise ValueError('Invalid host input')
        result = subprocess.check_output(['ping', '-c', '1', cmd_quote(host)], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'result': result}
    except subprocess.CalledProcessError as e:
        return JSONResponse(content={'error': str(e)}, status_code=500)

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid host input')
    result = subprocess.check_output(['ping', '-c', '1', cmd_quote(host)], stderr=subprocess.STDOUT, text=True)
    return {'status': 'completed', 'result': result}