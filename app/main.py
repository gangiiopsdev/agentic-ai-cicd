from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    if validate_host(host):
        args = ['ping', '--', host]
        subprocess.run(args, check=True)
        return {'status': 'completed'}
    else:
        raise ValueError('Invalid host')

def validate_host(host: str) -> bool:
    # Add validation logic here
    import re
    if re.match(r'^[a-zA-Z0-9.-]+$', host):
        return True
    return False