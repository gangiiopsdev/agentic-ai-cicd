from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str) -> bool:
    try:
        args = ["ping", host]
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return True
    except subprocess.CalledProcessError as e:
        print(e.stderr)
        return False
def ping(host: str):
    if not safe_ping(host):
        return {'status': 'failed'}
    return {'status': 'completed'}