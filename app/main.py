from fastapi import FastAPI
import subprocess
def ping(host: str):
    if not host.isdigit():
        raise ValueError('Invalid host input')
    # Safer implementation using subprocess.run with absolute path and shell=False
    subprocess.run(['ping', '-c', '1', '/sbin/ping'], check=True, capture_output=True, text=True)

class SafePing:
    @staticmethod
def ping_endpoint(host: str):
        return ping(host)