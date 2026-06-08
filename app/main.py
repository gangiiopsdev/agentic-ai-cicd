from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def secure_ping(host):
    allowed_hosts = ['127.0.0.1', 'localhost']
    if host in allowed_hosts:
        try:
            result = subprocess.run(['ping'], input=host, check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            raise ValueError('Ping failed') from e
    else:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    response = await secure_ping(host)
    return {'status': 'completed', 'output': response}