from fastapi import FastAPI
import subprocess
global allow_ping = False
def ping(host: str):
    global allow_ping
    if not allow_ping:
        return {'status': 'ping disabled'}

    # Secure implementation
    output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': output.stdout}