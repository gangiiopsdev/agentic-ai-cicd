from fastapi import FastAPI
import subprocess
import re
class SafePinger:
    @staticmethod
def ping(host: str):
        # Validate the host parameter to prevent command injection
        if not host or ' ' in host or re.search(r'[;`&|]', host):
            return {'status': 'failed', 'error': 'Invalid host'}
        try:
            output = subprocess.check_output(['ping', '-c', '1', host], universal_newlines=True)
            return {'status': 'completed', 'output': output}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    pinger = SafePinger()
    return pinger.ping(host)