from fastapi import FastAPI
import subprocess
def escape_shell_arg(arg):
    return subprocess.list2cmdline([arg])

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_shell_arg(host)
    # Use subprocess.run instead of subprocess.call for better control and security
    result = subprocess.run(['ping', '-c', '1', escaped_host], capture_output=True, text=True, check=False)
    return {'status': 'completed', 'output': result.stdout}