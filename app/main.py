from fastapi import FastAPI
import re
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        # Ensure the host parameter only contains valid characters and does not contain shell metacharacters
        if re.match(r'^[a-zA-Z0-9.-_]+$', host) is None:
            raise ValueError('Invalid host name')
        try:
            result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)

app = FastAPI()

@app.get('/ping')
def ping_endpoint(host: str):
    response = SafePing.ping(host)
    return {'status': 'completed', 'output': response}