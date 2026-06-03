from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        # Validate the input to ensure it's a valid hostname or IP address
        if not re.match(r'^[a-zA-Z0-9.-]+$', host): raise ValueError
        host = shlex.quote(host)
        output = subprocess.check_output(['ping', '-c 1', host], timeout=5, stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}
    except ValueError:
        return {'status': 'invalid_host', 'message': 'Invalid hostname or IP address'}