from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Create a list of arguments for the ping command instead of using shell=True
    args = ['ping', host]
    try:
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr.decode('utf-8')}'

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)