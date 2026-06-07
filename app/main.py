from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def escape_host(host):
    return ''.join(e for e in host if e.isalnum() or e.isdigit() or e in ('.', '-', '_'))

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    try:
        subprocess.call(['ping', shlex.quote(escaped_host)], shell=False)
        return {'status': 'completed'}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}