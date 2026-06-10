from fastapi import FastAPI
import subprocess
class SecurePing:
    def __init__(self):
        self.allowed_hosts = ['127.0.0.1', '::1']

    def ping(self, host: str):
        if host in self.allowed_hosts:
            try:
                result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
                return {"status": "completed", "output": result.stdout}
            except subprocess.CalledProcessError as e:
                return {"status": "error", "message": str(e)}
        else:
            return {"status": "invalid_host", "message": "Only localhost is allowed"}

app = FastAPI()
ping_service = SecurePing()

@app.get('/ping')
def ping(host: str):
    return ping_service.ping(host)