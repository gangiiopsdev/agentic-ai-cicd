from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def sanitize_input(input_string):
    # Implement a more robust sanitization function here
    return re.sub(r'[^a-zA-Z0-9\-_:.@]', '', input_string)

@app.get('/ping')
def ping(host: str):
    sanitized_host = subprocess.list2cmdline([sanitize_input(host)])
    try:
        result = subprocess.run(['ping', sanitized_host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}