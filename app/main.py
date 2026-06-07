from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(c for c in host if c in allowed_chars)

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    try:
        # Use a regular expression to validate the host input
        if not re.match(r'^[a-zA-Z0-9.-]+$', sanitized_host):
            raise ValueError("Invalid host")
        output = subprocess.run(['ping', '-c 1', '--', sanitized_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except (subprocess.CalledProcessError, ValueError) as e:
        return {'status': 'failed', 'error': str(e)}

if __name__ == '__main__':
    import uvicorn
    # Bind to a specific IP address instead of all interfaces
    uvicorn.run(app, host='127.0.0.1', port=8000)