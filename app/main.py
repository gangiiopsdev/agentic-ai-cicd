from fastapi import FastAPI
import subprocess
import shlex
git typing import List

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate host input (e.g., allowed IP ranges)
    try:
        ip_parts = host.split('.')
        if len(ip_parts) != 4 or any(not part.isdigit() for part in ip_parts) or any(int(part) > 255 for part in ip_parts):
            raise ValueError('Invalid host input')
    except Exception as e:
        return {'status': str(e)}

    # Use a safer alternative to subprocess if possible
    # For example, use library functions to perform ping operations safely
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
        return {'status': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': str(e)}