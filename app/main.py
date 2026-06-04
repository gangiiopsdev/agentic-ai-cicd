from fastapi import FastAPI
import subprocess
globals = {'ping': None'}
app = FastAPI()
def execute_ping(host):
    args = ['ping', host]
    if globals['ping'] is None:
        try:
            output = subprocess.run(args, shell=False, capture_output=True, text=True)
            globals['ping'] = output
        except Exception as e:
            print(f'Error executing ping: {e}')
@app.get("/ping")
def ping(host: str):
    # Secure implementation
    execute_ping(host)
    return {"status": "completed", "output": globals['ping'].stdout}