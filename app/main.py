from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation
    result = subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True)
    return {'status': 'completed', 'result': result.stdout}