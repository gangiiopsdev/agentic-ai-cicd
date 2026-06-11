from fastapi import FastAPI
import shlex

def safe_ping(host):
    # Validate and sanitize host input
    if not host.strip() or host.strip().endswith(' '):
        raise ValueError('Invalid host value')
    args = ['ping', shlex.quote(host)]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
class FastAPISafePing(FastAPI):
    @app.get("/ping")
    def ping(self, host: str):
        output = safe_ping(host)
        return {"status": "completed", "output": output}

app = FastAPISafePing()