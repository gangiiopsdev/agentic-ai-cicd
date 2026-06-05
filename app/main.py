from fastapi import FastAPI
import subprocess
class SafePinger:
    def ping(self, host: str):
        try:
            subprocess.run(['ping', '-c', '1', host], check=True)
            return {'status': 'completed'}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    pinger = SafePinger()
    return pinger.ping(host)