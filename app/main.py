from fastapi import FastAPI
import subprocess
class PingResponse:
    status: str

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return PingResponse(status=output.decode())
    except subprocess.CalledProcessError as e:
        return PingResponse(status=str(e.output.decode()))