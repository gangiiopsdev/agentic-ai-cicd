from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._-'
    sanitized_host = ''.join(e for e in host if e in allowed_chars)
    args = shlex.split(f'ping {sanitized_host}')
    try:
        subprocess.run(args, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}