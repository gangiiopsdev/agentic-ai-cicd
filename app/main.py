from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        try:
            result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'output': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_host(host: str):
    safe_ping = SafePing()
    return safe_ping.ping(host)