from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    # Implement input sanitization logic here, e.g., using regex or a whitelist of allowed characters
    return ''.join(c for c in input_str if c.isalnum() or c in '.-')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        result = subprocess.run(shlex.split('ping ' + sanitized_host), check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}