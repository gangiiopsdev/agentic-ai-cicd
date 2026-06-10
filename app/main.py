from fastapi import FastAPI
import subprocess
import shlex
import re
import os

def sanitize_input(input_str):
    return ''.join(c for c in input_str if c.isalnum() or c in ['.', ':', '-'])

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    host = sanitize_input(host)
    args = ['ping'] + shlex.split(re.escape(host))
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

# Preventive Controls:
# 1. Use parameterized queries or prepared statements if executing SQL commands.
# 2. Implement rate limiting to prevent brute force attacks.
# 3. Monitor and log suspicious activity.