from fastapi import FastAPI
class PingRequest:
    def __init__(self, host: str):
        self.host = host

@app.get("/ping")
def ping(request: PingRequest):
    try:
        response = subprocess.run(['ping', '-c 1', request.host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': response.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}