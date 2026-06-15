from fastapi import FastAPI
import re

app = FastAPI()

def sanitize_input(input_string):
    # Implement a more robust sanitization function here
    return ''.join(c for c in input_string if c.isalnum() or c in '-_.:@')

@app.get('/ping')
def ping(host: str):
    sanitized_host = subprocess.list2cmdline([sanitize_input(host)])
    try:
        result = subprocess.run(['ping', '-c', '1', sanitized_host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}