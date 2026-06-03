from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        try:
            # Safe implementation using subprocess.run
            result = subprocess.run(['ping', host], capture_output=True, text=True)
            return result.stdout
        except Exception as e:
            return str(e)

app = FastAPI()

@app.get("/ping")
def ping_route(host: str):
    response = SafePing.ping(host)
    return {'status': 'completed', 'output': response}