from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        # Secure implementation
        args = ['ping', host]
        subprocess.run(args, check=True)

app = FastAPI()

@app.get('/ping')
def ping_safe(host: str):
    safe_ping = SafePing()
    safe_ping.ping(host)
    return {'status': 'completed'}