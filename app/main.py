from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return result.stdout

def ping(host: str):
    # Secure implementation using safe_ping function
    response = safe_ping(host)
    return {'status': 'completed', 'response': response}