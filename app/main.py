from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.valid_hosts = set(['192.168.1.1', '10.0.0.1'])

    def ping(self, host: str):
        if host.strip() == '' or host not in self.valid_hosts:
            raise ValueError('Host cannot be empty or invalid')
        subprocess.run(['ping', '-c', '4', host], check=True)

app = FastAPI()
ping_instance = SafePing()

@app.get("/ping")
def ping_endpoint(host: str):  
    return ping_instance.ping(host)