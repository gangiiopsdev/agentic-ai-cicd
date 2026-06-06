from fastapi import FastAPI
import subprocess
def get_ip(host):
    try:
        result = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode != 0:
            raise Exception(result.stderr)
        return result.stdout
    except Exception as e:
        raise Exception(str(e))

app = FastAPI()
@app.get("/get-ip")
def get_ip_endpoint(host: str):
    return get_ip(host)