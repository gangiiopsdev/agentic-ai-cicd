from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        # Secure implementation
        args = ['ping', host]
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    safe_ping = SafePing()
    return safe_ping.ping(host)