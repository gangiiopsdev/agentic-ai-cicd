from fastapi import FastAPI
import asyncio
import os

app = FastAPI()

def safe_ping(host: str):
    try:
        if not host.isalnum():
            raise ValueError('Invalid hostname')
        args = ['ping', '-c', '1', host]
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except Exception as e:
        return {'error': str(e)}

@app.get('/ping')
def ping(host: str):
    safe_host = host  # Directly use the input without sanitization for this example, but consider further validation and escaping in production code.
    return safe_ping(safe_host)