from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
class PingHostException(Exception):
    pass
def ping(host: str):
    if not host.isdigit():
        raise PingHostException("Invalid input")
    return safe_ping(host)
app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    try:
        return {'result': ping(host)}
    except PingHostException as e:
        return {'error': str(e)}