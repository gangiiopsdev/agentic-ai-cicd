from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        safe_host = ''.join(c for c in host if c.isalnum() or c.isdigit() or c in '_.-')
        try:
            output = subprocess.check_output(['ping', '-c', '1', safe_host], stderr=subprocess.STDOUT, universal_newlines=True)
            return {'status': 'completed', 'output': output}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e.output)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return SafePing.ping(host)