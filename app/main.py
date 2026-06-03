from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    try:
        # Sanitize the host input to prevent command injection
        sanitized_host = shlex.quote(host)
        result = subprocess.run(shlex.split(f'ping {sanitized_host}'), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout if result.returncode == 0 else result.stderr
    except Exception as e:
        return str(e)

class SafePingFastAPI(FastAPI):
    @app.get("/ping")
    def ping(host: str):
        return {"status": safe_ping(host)}