from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        try:
            output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': output.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'output': e.stderr}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_ping = SafePing()
    return safe_ping.ping(host)