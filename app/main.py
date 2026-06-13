from fastapi import FastAPI
import subprocess
from shlex import quote
import os

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    try:
        output = subprocess.check_output(['ping', quote(host)], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

# Preventive Controls
# 1. Use absolute paths for executable commands.
# 2. Validate and sanitize user inputs.
# 3. Avoid using shell=True unless absolutely necessary.