from fastapi import FastAPI
import subprocess
import shlex
generate_safelist = ['google.com', 'example.com']

app = FastAPI()

def ping(host: str):
    if host in generate_safelist:
        try:
            command = ['ping', shlex.quote(host)]
            output = subprocess.run(command, capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': output.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}
    else:
        return {'status': 'failed', 'error': 'Invalid host'}