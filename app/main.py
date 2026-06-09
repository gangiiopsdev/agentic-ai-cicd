from fastapi import FastAPI
import subprocess
def safe_ping(host):
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout,

class FastAPISafePing(FastAPI):
    @app.get("/ping")
    def ping(self, host: str):
        return safe_ping(host)