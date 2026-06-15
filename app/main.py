from fastapi import FastAPI
import re
import shlex

app = FastAPI()

def ping(host: str):
    # Validate and sanitize host input using shlex.quote
    safe_host = shlex.quote(host)
    args = ['ping', safe_host]
    result = subprocess.run(args, capture_output=True, text=True, check=False, shell=False)
    return {'status': 'completed', 'output': result.stdout}