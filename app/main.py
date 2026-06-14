from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run()
    result = subprocess.run(['ping'] + shlex.split(host), check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}