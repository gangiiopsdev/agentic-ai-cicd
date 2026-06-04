from fastapi import FastAPI
import subprocess
class PingRequest:
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    valid_hosts = ['example.com', 'localhost']
    if request.host not in valid_hosts:
        return {'status': 'error', 'message': 'Invalid host'}
    args = ['ping', request.host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'result': result.stdout}