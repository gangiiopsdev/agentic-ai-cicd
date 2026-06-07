from fastapi import FastAPI
import re
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        # Validate the host to ensure it does not contain malicious characters or patterns
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            raise ValueError('Invalid host input')
        args = ['ping', host]
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    return {'status': 'completed', 'output': safe_ping(host)}