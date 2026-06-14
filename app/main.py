from fastapi import FastAPI
allowed_hosts = {'localhost', '127.0.0.1'}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host in allowed_hosts:
        result = subprocess.run(['ping', '-c', '1', '--interval=0.2', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'error': 'Host not allowed'}