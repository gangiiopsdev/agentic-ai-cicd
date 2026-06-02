from fastapi import FastAPI
import subprocess
def ping(host: str):
    if host and ' ' not in host:
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'status': 'error', 'message': 'Invalid input'}
app = FastAPI()
@app.get("/ping/")
def ping_route(host: str):  
    return ping(host)