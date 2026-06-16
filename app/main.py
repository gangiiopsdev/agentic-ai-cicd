from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def ping(host: str):
    # Improved regex to validate hostname more strictly
    if not re.match(r'^[a-zA-Z0-9.-]{1,255}$', host):
        raise ValueError('Invalid hostname')
    args = ['ping', '-c', '4', host]  # Use -c option for number of pings
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    return {'status': 'completed', 'output': result.stdout}