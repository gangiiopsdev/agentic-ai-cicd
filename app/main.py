from fastapi import FastAPI
import subprocess
import re
def safe_ping(host):
    # Enhanced validation using regex
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid hostname")
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
class PingRouter:
    app = FastAPI()

    @app.get("/ping")
    def ping(host: str):
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            raise ValueError("Invalid hostname")
        response = safe_ping(host)
        return {'status': 'completed', 'response': response}
PingRouter()