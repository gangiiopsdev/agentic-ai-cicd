from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        # Use check_output instead of call for better error handling and security.
        result = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'result': result}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e.output)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return ping(host)