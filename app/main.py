from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    for char in get_shell:
        if char in host:
            raise ValueError('Invalid characters in hostname')
    try:
        result = subprocess.run(['ping', f'"{host}"'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode()
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)