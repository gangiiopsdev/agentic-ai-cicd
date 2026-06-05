from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Using subprocess.call without shell=True and with a list of arguments
    try:
        subprocess.call(['ping', '-c', '1', host], timeout=5)
    except Exception as e:
        return False, str(e)
    return True, None

class SafePingFastAPI(FastAPI):
    @app.get("/ping")
    def ping(host: str):
        success, error = safe_ping(host)
        if not success:
            return {"status": "failed", "error": error}
        return {"status": "completed"}

app = SafePingFastAPI()