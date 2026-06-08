from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host.isnumeric():
        return {'error': 'Invalid input'}
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
class FastAPIApp(FastAPI):
    @app.get("/ping")
    def ping(host: str):
        return safe_ping(host)

app = FastAPIApp()