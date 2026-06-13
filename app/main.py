from fastapi import FastAPI
import subprocess
from shlex import quote

def sanitize_input(input_str):
    # Basic sanitization, improve as needed
    return ''.join(e for e in input_str if e.isalnum() or e in '-.:')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    result = subprocess.run(['ping', '-c', '1', quote(sanitized_host)], capture_output=True, text=True)
    return {'output': result.stdout}