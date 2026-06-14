from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def sanitize_input(value):
    return ''.join(e if e.isalnum() or e in ('.', '-', '_') else '_' for e in value)

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        result = subprocess.run(['ping', quote(sanitized_host)], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}