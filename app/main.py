from fastapi import FastAPI
import subprocess
def safe_ping(host):
    allowed_hosts = ['localhost', '127.0.0.1']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

class SafePingDependency:
    def __init__(self):
        self.allowed_hosts = ['localhost', '127.0.0.1']  # Define a list of allowed hosts

    async def ping(self, host: str):
        if host not in self.allowed_hosts:
            raise ValueError('Invalid host')
        output = safe_ping(host)
        return {'status': 'completed', 'output': output}

app = FastAPI()

@app.get("/ping")
def ping(host: str, depends=Depends(SafePingDependency())):
    return depends.ping(host)