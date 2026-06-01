from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host):
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout

app = FastAPI()

def ping(host: str):
    try:
        response = SafePing.safe_ping(host)
        return {"status": "completed", "output": response}
    except Exception as e:
        return {"status": "error", "message": str(e)}