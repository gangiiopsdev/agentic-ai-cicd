from fastapi import FastAPI
import subprocess
import shlex
def escape_shell(s):
    return ''.join(c if c.isalnum() or c in '_-./:' else '_' for c in s)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize the input to prevent command injection
    host = escape_shell(host)
    result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}