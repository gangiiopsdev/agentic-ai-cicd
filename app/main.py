from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def escape_host(host):
    host = host.replace(';', '').replace('&', '').replace('|', '')
    return host

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    # Use subprocess.run instead of subprocess.call and avoid passing the command as a string
    result = subprocess.run(shlex.split('ping ' + escaped_host), capture_output=True, text=True, check=False)
    return {'status': 'completed', 'output': result.stdout}