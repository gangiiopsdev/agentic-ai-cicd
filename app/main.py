from fastapi import FastAPI
import subprocess
class SafePing:
    ALLOWED_HOSTS = ['example.com', 'test.com']

    @staticmethod
def is_valid_host(host: str) -> bool:
        return any(host.endswith(allowed_host) for allowed_host in SafePing.ALLOWED_HOSTS)

    @staticmethod
def safe_ping(host: str):
        if not SafePing.is_valid_host(host):
            raise ValueError('Invalid host input')
        subprocess.run(['ping', '-c 1', host], check=True)
        return {'status': 'completed'}

global_app = FastAPI()

@global_app.get('/ping')
def ping_endpoint(host: str):
    try:
        return SafePing.safe_ping(host)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))