from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    @staticmethod
def run_safe_ping(host: str) -> dict:
        try:
            # Validate and sanitize input
            if not host.isalnum() or ' ' in host:
                return {'status': 'error', 'message': 'Invalid host name'}
            args = ['ping', *shlex.split(shlex.quote(host))]
            result = subprocess.run(args, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return SafePing.run_safe_ping(host)