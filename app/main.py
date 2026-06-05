from fastapi import FastAPI
import subprocess
from shlex import quote
import os

def sanitize_input(input_string):
    return ''.join(filter(str.isalnum, input_string))

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command = ['ping', quote(sanitized_host)]
    subprocess.run(command, check=True, shell=False, executable=None)
    return {'status': 'completed'}