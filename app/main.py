from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts

app = FastAPI()

@app.get("/ping")
def ping(host: str):\n    if validate_host(host):\n        args = ['ping', '--'] + [host]\n        subprocess.run(args, check=True)\n        return {'status': 'completed'}\n    else:\n        return {'status': 'error', 'message': 'Host not allowed'}, 403