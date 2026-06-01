from fastapi import FastAPI
import subprocess
class Ping:
    @staticmethod
def ping(host: str):
        # Safe implementation using check_output
        try:
            subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
            return {'status': 'completed'}
        except subprocess.CalledProcessError as e:
            return {'error': e.output.decode()}

app = FastAPI()

@app.get("/ping")
def ping_route(host: str):
    return Ping.ping(host)