from fastapi import FastAPI
import subprocess
import shlex
import re

def ping(host: str):
    try:
        # Sanitize the host input to prevent command injection
        if re.search(r'[;\&|`$()<>{}]', host, re.IGNORECASE) is not None:
            raise ValueError('Invalid input')
        args = ['ping', '-c', '1'] + shlex.split(host)
        output = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    except ValueError as ve:
        return {'status': 'failed', 'error': str(ve)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)