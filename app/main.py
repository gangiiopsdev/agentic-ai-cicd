from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(filter(str.isalnum, input_string))

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command = f'ping {sanitized_host}'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return {'output': result.stdout}