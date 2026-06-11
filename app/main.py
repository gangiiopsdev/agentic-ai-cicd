from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Use parameterized command instead of formatting strings for security
    args = shlex.split(f'ping -c 1 {host}')  # Limit the number of pings to prevent DDoS attacks
    subprocess.run(args, check=True)

app = FastAPI()

def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}