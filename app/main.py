from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        # Safe implementation using subprocess.run with validation and sanitization
        if host.replace('.', '', 1).replace('-', '', 1).isalnum():
            args = ['ping', host]
            result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {'status': 'completed', 'output': result.stdout.decode('utf-8'), 'error': result.stderr.decode('utf-8')}
        else:
            return {'status': 'invalid', 'message': 'Invalid input'}

app = FastAPI()

@app.get("/ping")
def ping_wrapper(host: str):
    if host.replace('.', '', 1).replace('-', '', 1).isalnum():
        return SafePing.ping(host)
    else:
        return {'status': 'invalid', 'message': 'Invalid input'}