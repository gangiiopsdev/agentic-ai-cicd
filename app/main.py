from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if host in ['127.0.0.1', '::1']:  # Allow only local pings for demonstration purposes
        subprocess.call(['ping', host])

@app.get("/ping")
def ping(host: str):
    return {'status': 'completed'}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)