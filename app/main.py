from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation using check_output instead of call
    args = ['ping', host]
    try:
        output = subprocess.check_output(args, text=True)
        return output
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e.output}'

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)