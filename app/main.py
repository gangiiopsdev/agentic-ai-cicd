from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.allowed_hosts = {'google.com', 'example.com'}

    def safe_ping(self, host: str):
        if host not in self.allowed_hosts:
            raise ValueError('Invalid hostname')
        args = ['ping', '-c', '4', host]
        subprocess.run(args, check=True)

app = FastAPI()
safe_ping_instance = SafePing()

@app.get("/ping")
def ping(host: str):
    safe_ping_instance.safe_ping(host)
    return {"status": "completed"}