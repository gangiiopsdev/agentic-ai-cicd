from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Using subprocess.run for a safer alternative
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def ping(host: str):
    # Using a safe function to avoid command injection
    return {'status': 'completed', 'result': safe_ping(host)}