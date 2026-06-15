from fastapi import FastAPI
import subprocess
global allowed_hosts = ['127.0.0.1', '::1']
app = FastAPI()
def escape_shell_arg(arg):
    return arg.replace(';', '').replace('&', '').replace('|', '')
@app.get("/ping")
def ping(host: str):
    if host not in allowed_hosts:
        return {'error': 'Host not allowed'}
safe_host = escape_shell_arg(host)
try:
    subprocess.run(['ping', safe_host], check=True, capture_output=True, text=True)
except subprocess.CalledProcessError as e:
    return {'error': e.stderr}
return {'status': 'completed'}