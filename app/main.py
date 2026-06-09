from fastapi import FastAPI
import subprocess
import shlex
def escape_host(host):
    return ''.join(e if e.isalnum() or e in '._-' else '_' for e in host)

def safe_ping(escaped_host):
    command = ['ping', '-c', '1', escaped_host]
    result = subprocess.run(command, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    escaped_host = shlex.quote(escape_host(host))
    return safe_ping(escaped_host)