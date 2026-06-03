from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    args = ['ping', '--', host]
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return result.stdout
class SafePing:
    @staticmethod
def safe_ping(host: str):
        return ping(host)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    try:
        output = SafePing.safe_ping(host)
        return {"status": "completed", "output": output}
    except Exception as e:
        return {"error": str(e)}