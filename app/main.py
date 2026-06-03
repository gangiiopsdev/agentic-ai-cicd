from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        # Safe implementation using subprocess.run with validation and sanitization
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout, 'error': result.stderr}

app = FastAPI()

@app.get("/ping")
def ping_wrapper(host: str):
    if all(c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-' for c in host):
        return SafePing.ping(host)
    else:
        return {'status': 'invalid', 'message': 'Invalid input'}