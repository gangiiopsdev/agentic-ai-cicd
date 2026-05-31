from fastapi import FastAPI
import subprocess
import re
class SafePing:
    @staticmethod
def ping(host: str):
        # Safe implementation using subprocess.run with validation and sanitization
        if re.match(r'^[a-zA-Z0-9.-]+$', host):  # Use regex to validate input
            args = ['ping', host]
            result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {'status': 'completed', 'output': result.stdout.decode('utf-8'), 'error': result.stderr.decode('utf-8')}
        else:
            return {'status': 'invalid', 'message': 'Invalid input'}

app = FastAPI()

@app.get("/ping")
def ping_wrapper(host: str):
    return SafePing.ping(host)}