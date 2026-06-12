from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    @staticmethod
def safe_ping(host: str) -> str:
        # Sanitize the host input to prevent shell injection
        sanitized_host = shlex.quote(host)
        command = f'ping {sanitized_host}'
        args = shlex.split(command)
        subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return 'completed'

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    result = SafePing.safe_ping(host)
    return {"status": result}