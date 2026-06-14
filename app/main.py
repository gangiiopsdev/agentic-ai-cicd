from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(filter(str.isalnum, input_string))

def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = ['ping', '-c', '1'] + shlex.split(shlex.quote(sanitized_host))  # Use a safe way to pass arguments
    subprocess.run(args, check=True)
    return {'status': 'completed'}