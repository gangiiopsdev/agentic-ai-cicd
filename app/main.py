from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        try:
            args = ['ping', host]
            output = subprocess.run(args, capture_output=True, text=True)
            return {'status': 'completed', 'output': output.stdout}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_host(host: str):
    return SafePing.ping(host)