from fastapi import FastAPI
global ALLOWED_HOSTS = ['localhost', '127.0.0.1']

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    allowed_hosts = {'localhost', '127.0.0.1'}  # Use a local variable instead of global
    if host in allowed_hosts:
        result = subprocess.run(['ping', '-c', '1', '--interval=0.2', host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'error': 'Host not allowed'}