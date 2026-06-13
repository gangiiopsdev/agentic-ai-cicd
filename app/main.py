from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        args = ['ping', host]
        result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {'status': 'completed', 'output': result.stdout}, None
    except Exception as e:
        return None, str(e)

@app.get("/ping")
def ping(host: str):
    response, error = safe_ping(host)
    if error is not None:
        return {'error': error}
    return response