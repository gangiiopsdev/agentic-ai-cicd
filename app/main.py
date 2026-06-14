from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_string):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    sanitized_input = ''.join(char for char in input_string if char in allowed_chars)
    return sanitized_input

app = FastAPI()

def execute_ping(host):
    try:
        output = subprocess.check_output(shlex.split(f'ping {host}'), stderr=subprocess.STDOUT, text=True)
        return output
    except subprocess.CalledProcessError as e:
        return str(e.output)

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    result = execute_ping(sanitized_host)
    return {"status": "completed", "result": result}