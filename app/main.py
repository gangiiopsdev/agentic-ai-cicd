from fastapi import FastAPI
import re

def ping(host: str):
    # Validate input to ensure it only contains allowed characters
    if re.match(r'^[a-zA-Z0-9.-]+$', host):
        result = subprocess.run(['ping', '--'] + [host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        raise ValueError('Invalid input')