from fastapi import FastAPI
import shlex
def safe_ping(host):
    # Validate and sanitize host input
    if not host.strip() or host.strip().endswith(' '):
        raise ValueError('Invalid host value')
    args = ['ping', '--'] + [shlex.quote(arg) for arg in host.split()]
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode().strip()
class FastAPISafePing(FastAPI):
    @app.get("/ping")
    async def ping(self, host: str):
        output = safe_ping(host)
        return {"status": "completed", "output": output}

app = FastAPISafePing()