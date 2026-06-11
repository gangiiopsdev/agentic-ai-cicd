from fastapi import FastAPI
import subprocess
def ping(host: str):
    if not host.isdigit():
        raise ValueError('Invalid host input')
    # Safer implementation using subprocess.run with absolute path and shell=False
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
class SafePing:
    @staticmethod
def ping_endpoint(host: str):
        return ping(host)