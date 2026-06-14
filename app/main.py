from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Replace with a secure method to ping the host
        response = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
        return response.stdout
    except Exception as e:
        return str(e)

def ping(host: str):
    return {'status': safe_ping(host)}