from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host):
        try:
            result = subprocess.run(['ping', '-c', '1', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            return result.stdout.strip()
        except Exception as e:
            return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    result = SafePing.safe_ping(host)
    return {"status": "completed", "result": result}