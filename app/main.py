from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize input
    if not host or len(host) > 255 or '.' not in host:
        raise ValueError('Invalid host input')
    args = ['ping', '-c', '1', '--', host]
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    return {'status': 'completed', 'output': result.stdout}

# Preventive Controls:
# 1. Use a whitelist of allowed hosts.
# 2. Sanitize input further (e.g., using regular expressions).
# 3. Consider using an alternative method if possible, such as HTTP ping APIs.