from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    # Add your input sanitization logic here, e.g., regex validation or allowed list of hosts.
    return ''.join(c for c in input_str if c.isalnum() and c not in '<>"&|;`*?{}[]^\\')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        sanitized_host = sanitize_input(host)
        result = subprocess.run(['ping', sanitized_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}