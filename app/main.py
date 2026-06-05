from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

def execute_ping(host):
    try:
        args = ['ping', host]
        if os.name == 'nt':
            args.append('-c')
        subprocess.run(args, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)