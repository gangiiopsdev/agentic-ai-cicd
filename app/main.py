from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_string):
    # Implement input sanitization logic here (e.g., whitelist of allowed characters)
    return ''.join(filter(str.isalnum, input_string))

@app.get("/ping")
def ping(host: str):
    sanitized_host = shlex.quote(sanitize_input(host))
    try:
        subprocess.call(['ping', '-c', '1', sanitized_host], timeout=5)
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}
    return {'status': 'completed'}