from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_valid_host(host):
    allowed_hosts = ['example.com', 'test.com']  # Define a list of allowed hosts
    return host in allowed_hosts

def sanitize_input(input_str):
    sanitized_input = input_str.strip()
    if not all(char.isalnum() or char in '.-' for char in sanitized_input):
        raise ValueError('Invalid characters in input')
    return sanitized_input

@app.get("/ping")
def ping(host: str):
    if is_valid_host(sanitize_input(host)):
        command = ['ping', '-c', '1', host]
        result = subprocess.run(command, capture_output=True, text=True)
        return {'output': result.stdout}
    else:
        return {'error': 'Invalid host'}