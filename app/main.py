from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def escape_host(host):
    host = host.replace(';', '').replace('&', '').replace('|', '')
    return host

def execute_command(command, args):
    try:
        result = subprocess.run([command] + args, capture_output=True, text=True, check=False)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

@app.get("/ping")
def ping(host: str):
    escaped_host = quote(escape_host(host))
    # Execute the command safely
    return execute_command('ping', [escaped_host])