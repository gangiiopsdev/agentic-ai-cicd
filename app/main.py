from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Safe implementation
    command = ['ping', host]
    result = subprocess.run(command, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}