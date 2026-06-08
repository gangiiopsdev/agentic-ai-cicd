from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation
    args = ['ping', host]
    subprocess.run(args, check=True, capture_output=True)
app = FastAPI()
@app.get("/ping")
def ping_route(host: str):
    try:
        result = ping(host)
        return {'result': result.stdout.decode()}
    except Exception as e:
        return {'error': str(e)}