from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        # Secure implementation
        try:
            result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
            return {'stdout': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'stderr': e.stderr}, 500

global ping
ping = SafePing.ping

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)