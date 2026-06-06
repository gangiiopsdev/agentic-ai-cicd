from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        args = ['ping', '-c', '1', host]
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
def ping(host: str):
    response = safe_ping(host)
    return {'status': 'completed', 'response': response}