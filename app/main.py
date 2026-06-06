from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Using subprocess.run with shell=False and with a list of arguments
    try:
        result = subprocess.run(['ping', '-c', '1', host], timeout=5, capture_output=True, text=True, check=True)
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, str(e.stderr)
    except Exception as e:
        return False, str(e)

class SafePingFastAPI(FastAPI):
    @app.get("/ping")
    def ping(host: str):
        success, error = safe_ping(host)
        if not success:
            return {"status": "failed", "error": error}
        return {"status": "completed", "output": error}

app = SafePingFastAPI()