from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(filter(str.isalnum, input_string))

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host.isdigit():  # Example simple validation
        return {'error': 'Invalid input'}, 400
    subprocess.call(['ping', sanitized_host])
    return {'status': 'completed'}