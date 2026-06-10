from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e in ('.', '-', '_'))

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent command injection
    safe_host = sanitize_input(host)
    result = subprocess.run(['ping', '-c', '1'], capture_output=True, text=True, input=safe_host.encode('utf-8'))
    return {'status': 'completed', 'output': result.stdout}