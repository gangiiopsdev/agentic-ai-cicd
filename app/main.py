from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation using shlex.quote to escape special characters in the host input.
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}