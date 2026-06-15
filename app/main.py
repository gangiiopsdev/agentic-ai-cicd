from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(c if c.isalnum() or c in '-.' else '_' for c in input_string)

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = ['ping', '-c 1', sanitized_host]
    subprocess.run(args, check=True, shell=False)
    return {'status': 'completed'}