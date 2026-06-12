from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def ping(host: str):
        try:
            output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, timeout=5)
            return {"status": "completed", "output": output.decode('utf-8')}
        except subprocess.CalledProcessError as e:
            return {"status": "error", "error": e.output.decode('utf-8')}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    if 'ping' not in host and '-' not in host:
        return SafeSubprocess.ping(host)
    else:
        return {"status": "error", "error": "Invalid input detected"}