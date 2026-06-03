from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5, shell=False)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}
    except Exception as e:
        return {"status": "failed", "error": str(e)}

@app.get("/ping")
def ping_wrapper(host: str):
    if 'localhost' in host or '127.0.0.1' in host:
        return ping(host)
    else:
        return {"status": "failed", "error": "Host not allowed"}