from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        try:
            output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, text=True)
            return output
        except subprocess.CalledProcessError as e:
            return str(e.output)

app = FastAPI()

@app.get("/ping")
def ping_host(host: str):
    safe_ping = SafePing()
    result = safe_ping.ping(host)
    return {'status': 'completed', 'result': result}