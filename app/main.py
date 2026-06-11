from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host: str) -> bool:
    return all(c.isalnum() or c.isdigit() for c in host)

async def ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid input")
    args = ['ping', shlex.quote(host)]
    result = await subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed', 'output': result.stdout.decode()}

app.get('/ping')(ping)