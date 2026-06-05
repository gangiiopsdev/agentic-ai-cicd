from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_host(host):
    # Basic escaping for demonstration. In production, consider using safe libraries or methods.
    return host.replace(';', '').replace('&', '')

@app.get("/ping")
def ping(host: str):

    # Secure implementation
    subprocess.call(['ping', escape_host(host)])

    return {"status": "completed"}