from fastapi import FastAPI
import re
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        # Use a whitelist approach instead of blacklist
        allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_.-')
        if not all(char in allowed_chars for char in host):
            return {'status': 'failed', 'error': 'Invalid input'}
        try:
            output = subprocess.check_output(['ping', '-c', '1', re.escape(host)], stderr=subprocess.STDOUT, universal_newlines=True)
            return {'status': 'completed', 'output': output}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e.output)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Enhanced validation input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9_.-]+$', host):
        return {'status': 'failed', 'error': 'Invalid input'}
    return SafePing.ping(host)