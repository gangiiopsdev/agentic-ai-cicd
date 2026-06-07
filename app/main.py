from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Using subprocess.run instead of subprocess.call for better control and security
        result = subprocess.run(['ping', host], check=True, text=True, capture_output=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.stderr}