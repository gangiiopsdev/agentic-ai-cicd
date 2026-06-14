from fastapi import FastAPI
import subprocess
import shlex
class InputFilter:
    def __init__(self):
        self.allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'

    def filter(self, input_str):
        return ''.join(char for char in input_str if char in self.allowed_chars)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    filtered_host = InputFilter().filter(host)
    try:
        result = subprocess.run(['ping', filtered_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'stdout': e.stdout.decode(), 'stderr': e.stderr.decode()}