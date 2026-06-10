from fastapi import FastAPI
import subprocess
global shell_check
shell_check = False

app = FastAPI()

def execute_ping(host):
    try:
        result = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    return {'status': execute_ping(host)}