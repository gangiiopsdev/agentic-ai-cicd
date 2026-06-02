from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

domain_regex = r'^[a-zA-Z0-9.-]+$'
path_regex = r'^(/[a-zA-Z0-9.-]+)*$'

@app.get(
    '/',
    summary='Agentic Self-Healing Pipeline',
    description='This is a simple API that returns a message.'
)
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get(
    '/ping',
    summary='Ping a host',
    description='Pings the specified host and returns the output.',
    responses={200: {'description': 'Successful response'}, 422: {'description': 'Validation error'}}
)
def ping(host: str):
    # Validate and sanitize input
    domain_parts = shlex.split(host)
    if not all(re.match(domain_regex, part) for part in domain_parts):
        raise ValueError('Invalid hostname')
    command = ['ping'] + [shlex.quote(part) for part in domain_parts]
    result = subprocess.run(command, shell=False, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}