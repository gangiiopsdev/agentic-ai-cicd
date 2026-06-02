from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    malicious_chars = ['&&', ';', '|', '`']
    for char in malicious_chars:
        if char in input_str:
            return False
    return True

@app.get('/ping')
def ping(host: str):
    if not sanitize_input(host):
        return {'status': 'error', 'message': 'Invalid input'}
    output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': output.stdout}
try:
    ping('example.com')
except subprocess.CalledProcessError as e:
    print(str(e))