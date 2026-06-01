from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    try:
        result = subprocess.run(shlex.split('ping -c 1 ' + host), capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

class FastAPIApp(FastAPI):
    @app.get("/ping")
    def ping(host: str):
        # Secure implementation
        output = safe_ping(host)
        return {"status": "completed", "output": output}

app = FastAPIApp()