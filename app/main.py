from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return output.decode('utf-8')
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    result = execute_ping(f'"{host}"')  # Escape host input to mitigate injection
    return {"status": "completed", "result": result}