from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        try:
            output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
            return output.decode('utf-8')
        except subprocess.CalledProcessError as e:
            return f'Failed to ping {host}: {e.output.decode('utf-8')}'

app = FastAPI()

@app.get("/ping")
def ping_safe(host: str):
    return SafePing.ping(host)