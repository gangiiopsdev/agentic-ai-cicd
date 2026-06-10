from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
class FastAPISafePing(FastAPI):
    @app.get("/ping")
    def ping(self, host: str):
        output = safe_ping(host)
        return {"status": "completed", "output": output}
app = FastAPISafePing()