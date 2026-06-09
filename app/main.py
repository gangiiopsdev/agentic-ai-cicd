from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation
    args = ['ping', host]
    result = subprocess.run(args, check=True, capture_output=True)
    return result.stdout.decode()
app = FastAPI()
@app.get("/ping")
def ping_route(host: str):
    try:
        result = ping(host)
        return {'result': result}
    except Exception as e:
        return {'error': str(e)}