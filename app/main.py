from fastapi import FastAPI
import shlex
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Regular expression to validate allowed hostnames
    pattern = r'^example\.com$|^test\.example\.com$'  # Replace with actual regex pattern
    if not re.match(pattern, host):
        raise ValueError('Invalid hostname')

    command = ['ping', shlex.quote(host)]
    result = subprocess.run(command, check=True, text=True, capture_output=True)

    return {'status': 'completed', 'output': result.stdout}