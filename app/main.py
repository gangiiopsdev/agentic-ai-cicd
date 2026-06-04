from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(filter(lambda x: x in allowed_chars, input_str))

@app.get('/ping')
def ping(host: str):    sanitized_host = shlex.quote(sanitize_input(host))
    subprocess.call(['ping', '-c', '1', sanitized_host])
    return {'status': 'completed'}