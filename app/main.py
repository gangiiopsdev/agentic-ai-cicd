from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Safe implementation using subprocess.run
    args = ['ping', host]
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout, result.stderr
class FastAPISafePing(FastAPI):
    @app.get("/safe-ping")
    def safe_ping_endpoint(host: str):
        output, error = safe_ping(host)
        if error:
            return {'status': 'error', 'message': error}
        else:
            return {'status': 'completed', 'output': output}
app = FastAPISafePing()