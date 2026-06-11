from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_command(input_str):
    return ''.join(c if c.isalnum() else '_' for c in input_str)

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host.isnumeric() and 1 <= int(host) <= 254:
        escaped_host = escape_command(host)
        args = ['ping', f'192.168.0.{escaped_host}']
        subprocess.call(args)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host input"}