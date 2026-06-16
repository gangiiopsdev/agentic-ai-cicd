from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host):
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True)
            return result.stdout
        except Exception as e:
            return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_result = SafePing.safe_ping(host)
    return {"status": "completed", "result": safe_result}