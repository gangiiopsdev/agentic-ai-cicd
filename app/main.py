from fastapi import FastAPI
import re

class SafePing:
    @staticmethod
def ping(host: str):
        # Ensure the host parameter only contains valid characters and does not contain shell metacharacters
        if re.match(r'^[a-zA-Z0-9.-_]+$', host) is None:
            raise ValueError('Invalid host name')
        try:
            import os
            result = os.popen(f'ping -c 1 {host}').read()
            return result
        except subprocess.CalledProcessError as e:
            return str(e)

app = FastAPI()

@app.get('/ping')
def ping_endpoint(host: str):
    response = SafePing.ping(host)
    return {'status': 'completed', 'output': response}