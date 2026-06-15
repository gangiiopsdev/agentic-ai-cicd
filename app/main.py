from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def escape_host(host: str) -> str:
        return ''.join(e if e.isalnum() else '_' for e in host)

def ping(host: str):
    safe_host = SafeSubprocess.escape_host(host)
    # Secure implementation
    subprocess.call(['ping', f'"{safe_host}"'], check=True)

app = FastAPI()

@app.get("/ping")
def ping_route(host: str):
    return ping(host)