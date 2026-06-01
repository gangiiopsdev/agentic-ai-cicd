from fastapi import FastAPI
import subprocess
import re
class SafePing:
    @staticmethod
def ping(host: str):
        # Safe implementation using subprocess.run with validation and sanitization
        if re.match(r'^[a-zA-Z0-9.-]+$', host):  # Use regex to validate input
            args = ['ping', host]
            try:
                result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
                return {'status': 'completed', 'output': result.stdout.decode('utf-8'), 'error': ''}
            except subprocess.CalledProcessError as e:
                return {'status': 'failed', 'output': '', 'error': str(e)}
        else:
            return {'status': 'invalid', 'message': 'Invalid input'}

app = FastAPI()

@app.get("/ping")
def ping_wrapper(host: str):
    return SafePing.ping(host)}