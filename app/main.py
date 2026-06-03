from fastapi import FastAPI
import subprocess
import re
def safe_ping(host: str):
    # Validate host input
    if not re.match(r'^[a-zA-Z0-9]{1,64}$', host):
        raise ValueError('Invalid input')
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, check=True, capture_output=True, text=True, shell=False)
    return result.stdout
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    try:
        output = safe_ping(host)
        return {'status': 'completed', 'output': output}
    except ValueError as e:
        return {'status': 'error', 'message': str(e)}