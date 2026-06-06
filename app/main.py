from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

def execute_ping(host):
    try:
        args = ['ping', host]
        if os.name == 'nt':
            args.append('-c')
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'error': str(e), 'output': str(e.output)}

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)