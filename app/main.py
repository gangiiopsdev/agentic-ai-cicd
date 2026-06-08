from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self, host):
        self.host = host

    async def run(self):
        try:
            result = subprocess.run(['ping', self.host], check=True, capture_output=True, text=True)
            return {'host': self.host, 'result': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'host': self.host, 'error': e.stderr}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    safe_ping_instance = SafePing(host)
    return await safe_ping_instance.run()