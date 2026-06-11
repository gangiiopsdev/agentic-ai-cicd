from fastapi import FastAPI
import re
import subprocess
class SafeSubprocess:
    @staticmethod
def ping(host: str):
        # Use regex to validate the host input
        if not re.match(r'^[a-zA-Z0-9-]+$', host):
            raise ValueError("Invalid host input")
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {
            "status": "completed",
            "output": result.stdout.decode()
        }
    except subprocess.CalledProcessError as e:
        return {
            "status": "failed",
            "error": str(e)
        }

app = FastAPI()

@app.get("/ping")
def ping_wrapper(host: str):
    return SafeSubprocess.ping(host)