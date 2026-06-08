from fastapi import FastAPI
import subprocess
from shlex import quote as shell_quote

app = FastAPI()

def sanitize_input(input_string):
    # Implement input sanitization logic here
    return ''.join(filter(str.isalnum, input_string))

@app.get('/ping')
def ping(host: str):
    host = sanitize_input(host)
    result = subprocess.run(['ping', shell_quote(host)], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}