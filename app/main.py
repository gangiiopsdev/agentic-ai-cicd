from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    if any(char in input_string for char in [';', '&', '|', '*', '?', '>', '<', '\', '$', '`']):
        return False
    return True

@app.get('/ping')
def ping(host: str):
    if not sanitize_input(host):
        return {'status': 'error', 'message': 'Invalid characters in host parameter'}
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}