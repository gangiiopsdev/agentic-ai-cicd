from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    args = ['ping', host]
    for arg in args:
        if isinstance(arg, list):
            args.extend(arg)
        else:
            args.append(arg)
    subprocess.run(args, check=True)

def ping(host: str):
    try:
        safe_ping(host)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}