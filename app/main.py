from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def is_safe_hostname(hostname):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return all(char in allowed_chars for char in hostname)

def validate_input(input_string):
    # Regular expression to allow only safe characters and patterns
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, input_string) is not None

@app.get('/ping')
def ping(host: str):\n    if not validate_input(host):\n        return {"status": "failed", "error": "Invalid hostname"}\n    try:\n        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)\n        return {"status": "completed", "output": result.stdout}\n    except subprocess.CalledProcessError as e:\n        return {"status": "failed", "error": str(e)}