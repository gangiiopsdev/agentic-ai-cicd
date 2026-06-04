from fastapi import FastAPI
import subprocess
def escape_shell_argument(value):
    return value.replace(';', '').replace('&', '')

global_config = {
    'allowed_hosts': ['example.com', 'localhost']
}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host in global_config['allowed_hosts']:
        escaped_host = escape_shell_argument(host)
        subprocess.call(f"ping {escaped_host}", shell=False)
        return {"status": "completed"}
    else:
        return {"status": "host not allowed"}