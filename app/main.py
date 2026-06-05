from fastapi import FastAPI
import subprocess
def escape_shell_arg(arg):
    return subprocess.list2cmdline([arg])

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input to prevent path traversal
    if not host.startswith('http://') and not host.startswith('https://'):
        return {'error': 'Invalid host'}, 400
    escaped_host = escape_shell_arg(host)
    # Perform the necessary operation with the escaped host
    result = subprocess.run(['ping', escaped_host], capture_output=True, text=True)
    return result.stdout