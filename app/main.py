from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def validate_input(input_string):
    if not all(c.isalnum() for c in input_string):
        raise ValueError("Invalid input")

@app.get('/ping')
def ping(host: str):
    try:
        validate_input(host)
        command = ['ping', host]
        args = shlex.split(' '.join(command))
        result = subprocess.run(args, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except ValueError as e:
        return {'error': str(e)}, 400