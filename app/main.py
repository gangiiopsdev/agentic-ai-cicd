from fastapi import FastAPI
import socket
import re
class SafePing:
    @staticmethod
def ping(host: str):
        # Robust implementation using regex and DNS resolution for validation and sanitization
        if re.match(r'^[a-zA-Z0-9.-]+$', host):  # Use regex to validate input
            try:
                socket.gethostbyname(host)  # Resolve the hostname
                args = ['ping', host]
                result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                return {'status': 'completed', 'output': result.stdout.decode('utf-8'), 'error': result.stderr.decode('utf-8')}
            except socket.gaierror:
                return {'status': 'invalid', 'message': 'Invalid hostname'}
        else:
            return {'status': 'invalid', 'message': 'Invalid input'}

app = FastAPI()

@app.get("/ping")
def ping_wrapper(host: str):
    return SafePing.ping(host)}