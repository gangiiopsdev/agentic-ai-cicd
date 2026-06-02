from fastapi import FastAPI
import subprocess
import shlex

def escape_host(host):
    host = host.replace(';', '').replace('&', '').replace('|', '')
    return host

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    # Use subprocess.run instead of subprocess.call and avoid passing the command as a string
    result = subprocess.run(['ping', shlex.quote(escaped_host)], capture_output=True, text=True, check=False, shell=False)
    return {'status': 'completed', 'output': result.stdout}