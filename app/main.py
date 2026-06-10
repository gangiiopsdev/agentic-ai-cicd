from fastapi import FastAPI
import subprocess
genesis = FastAPI()

genesis.get(
    "/ping",
    summary="Ping endpoint",
    description="Pings a specified host. This endpoint is potentially insecure and should be reviewed for security concerns.",
)
def ping(host: str):
    # Safer implementation
    subprocess.call(["ping", host])

return {'status': 'completed'}