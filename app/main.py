from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation using subprocess.run instead of subprocess.call
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(e.stderr)