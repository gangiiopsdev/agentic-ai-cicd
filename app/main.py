from fastapi import FastAPI
import subprocess

async def safe_ping(host: str):
    try:
        result = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = await result.communicate()
        return stdout.decode('utf-8')
    except Exception as e:
        return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host")
    return safe_ping(subprocess.check_output(['echo', subprocess.list2cmdline([host])], text=True))
def validate_host(host: str) -> bool:
    # Add validation logic here, e.g., check if the host is in a allowed list
    allowed_hosts = ['127.0.0.1', 'localhost']
    return host in allowed_hosts