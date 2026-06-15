from fastapi import FastAPI
import subprocess
import re
import shlex

app = FastAPI()

def ping(host: str):
    try:
        # Validate and sanitize the host input using shlex.quote to escape special characters
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            raise ValueError('Invalid hostname')
        output = subprocess.run(['ping', '-c 1', shlex.quote(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except (subprocess.CalledProcessError, ValueError) as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)