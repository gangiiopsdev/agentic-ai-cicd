from fastapi import FastAPI
import subprocess
class SafePinger:
    def __init__(self):
        self.allowed_hosts = ['example.com', 'localhost']

    def ping(self, host):
        if host not in self.allowed_hosts:
            raise ValueError('Invalid host')
        args = ['ping', subprocess.check_output(['echo', host]).decode().strip()]
        result = subprocess.run(args, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}

app = FastAPI()
pinger = SafePinger()

@app.get("/ping")
def ping(host: str):
    return pinger.ping(host)