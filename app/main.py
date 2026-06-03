from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        # Secure implementation using subprocess.run with validation and sanitization
        sanitized_host = ''.join(c for c in host if c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
        args = ['ping', '-c', '1', sanitized_host]
        result = subprocess.run(args, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout, 'error': result.stderr}

app = FastAPI()

@app.get("/ping")
def ping_wrapper(host: str):
    sanitized_host = ''.join(c for c in host if c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
    return SafePing.ping(sanitized_host)