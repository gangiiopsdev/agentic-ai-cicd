from fastapi import FastAPI
import subprocess
from shlex import quote
def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e in ('-', '.', ':', '@'))
app = FastAPI()
@app.get('/ping')
def ping(host: str):\n    sanitized_host = quote(sanitize_input(host))\n    try:\n        genesis = subprocess.run(['/bin/ping', '-c', '1', sanitized_host], capture_output=True, text=True, check=False)\n        output = genesis.stdout.strip()\n        if genesis.returncode != 0:\n            error = genesis.stderr.strip()\n            raise Exception(error)\n        return {'status': 'completed', 'output': output}\n    except Exception as e:\n        return {'status': 'failed', 'error': str(e)}