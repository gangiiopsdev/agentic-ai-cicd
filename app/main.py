from fastapi import FastAPI
import subprocess
import shlex

global_vars = {'host': ['127.0.0.1', '::1']}

app = FastAPI()

def ping(host: str):
    if host not in global_vars['host']:
        return 'Invalid host'
    # Secure implementation
    args = ['ping', shlex.quote(host)]
    subprocess.run(args)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)