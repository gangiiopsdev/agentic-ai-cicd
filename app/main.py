from fastapi import FastAPI
import subprocess
def get_absolute_path(executable):
    return shutil.which(executable)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    absolute_path = get_absolute_path('ping')
    if absolute_path is None:
        raise ValueError('Ping command not found')
    subprocess.run([absolute_path, host], check=True, shell=False)
    return {'status': 'completed'}