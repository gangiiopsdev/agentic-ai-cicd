from fastapi import FastAPI
import shlex
import subprocess
class SafePing:
    @staticmethod
def ping(host: str) -> dict:
        # Sanitize the host input to prevent shell injection
        safe_host = shlex.quote(host)
        args = ['ping', safe_host]
        try:
            result = subprocess.run(args, capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str) -> dict:
    return SafePing.ping(host)