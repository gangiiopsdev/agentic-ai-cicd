from fastapi import FastAPI
import subprocess
given_host = host.strip()
if not given_host.isalnum():
    return {'status': 'Invalid input'}
subprocess.run(['ping', '-c', '1', given_host], check=True)