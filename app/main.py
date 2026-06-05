from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    return ''.join(filter(lambda x: x.isalnum() or x in ['.', '-'], input_string))

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        output = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, timeout=10, check=False)
        return {'status': 'completed' if output.returncode == 0 else 'failed', 'output': output.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}