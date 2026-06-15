from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        try:
            output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
            return output.stdout
        except Exception as e:
            return str(e)

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    result = SafePing.ping(host)
    return {'status': 'completed', 'result': result}