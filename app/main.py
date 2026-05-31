from fastapi import FastAPI
import subprocess
import shlex
import os

def sanitize_input(input_string):
    safe_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_\n\t'
    return ''.join(filter(lambda x: x in safe_chars, input_string))

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    sanitized_host = sanitize_input(host)
    output = subprocess.check_output(['ping', sanitized_host], stderr=subprocess.STDOUT, timeout=5)
    return {"status": "completed", "output": output.decode()}
except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
    return {"status": "failed", "error": str(e)}