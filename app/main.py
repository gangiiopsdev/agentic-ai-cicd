from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Safe implementation using check_output and avoiding shell=True
        result = subprocess.check_output(["ping", host], timeout=5)
        return True, result.decode()
    except subprocess.CalledProcessError as e:
        return False, str(e)
    except Exception as e:
        return False, str(e)

@app.get("/ping")
def ping(host: str):
    success, output = safe_ping(host)
    if success:
        return {"status": "completed", "result": output}
    else:
        return {"status": "failed", "error": output}