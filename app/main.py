from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(e.stderr)