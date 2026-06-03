from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host or not re.match(r'^[a-zA-Z0-9]+$', host):
        return {'status': 'error', 'message': 'Invalid host'}
    command = ['ping', host]
    result = subprocess.run(command, capture_output=True, text=True)
    # Sanitize output to prevent XSS or other attacks
    sanitized_output = re.sub(r'<.*?>', '', result.stdout)
    return {'status': 'completed', 'output': sanitized_output}