from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e in ['.', '-'])

@app.get('/ping')
def ping(host: str):
    host = sanitize_input(host)
    args = ['ping', host]
    # Use subprocess.run instead of subprocess.call for better control and security
    result = subprocess.run(args, shell=False, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}