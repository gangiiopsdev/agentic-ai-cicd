from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f'Error pinging {host}: {str(e)}'

def ping(host: str):
    response = safe_ping(host)
    return {'status': 'completed', 'result': response}