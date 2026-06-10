from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_string):
    safe_string = ''.join(c if c.isalnum() or c in ['-', '.', '_', ':'] else '_' for c in input_string)
    return safe_string

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = ['ping', sanitized_host]
    result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}

# Enhanced sanitization to avoid command injection
import re

def enhanced_sanitize_input(input_string):
    if re.search(r'[^a-zA-Z0-9-.:_ ]', input_string):
        raise ValueError('Invalid characters in host name')
    return input_string

@app.get('/ping')
def ping(host: str):
    sanitized_host = enhanced_sanitize_input(host)
    args = ['ping', sanitized_host]
    result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}