from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e in [',', '.', '-', '_', ' ', '!'])

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = host.replace('-', '')  # Sanitize to avoid shell injection
    result = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}