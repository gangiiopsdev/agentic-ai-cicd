from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(filter(str.isalnum, input_str))

@app.get("/ping")
def ping(host: str):
    # Sanitize and validate host input
    host = sanitize_input(host)
    if not host:
        return {'error': 'Invalid host'}, 400

    args = ['ping', shlex.quote(host)]
    subprocess.run(args, check=True, shell=False)

    return {'status': 'completed'}