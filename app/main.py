from fastapi import FastAPI
import subprocess
def escape_shell_arg(arg):
    return ''.join(c for c in arg if c.isalnum() or c in '-_.:/@&=+$,;')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    escaped_host = escape_shell_arg(host)
    subprocess.call(['ping', '--', escaped_host])  # Add -- to prevent injection
    return {'status': 'completed'}