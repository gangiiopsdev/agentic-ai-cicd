from fastapi import FastAPI
import re

def ping(host: str):
    # Secure implementation
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):  # Improved regex for hostname validation
        raise ValueError('Invalid hostname')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}