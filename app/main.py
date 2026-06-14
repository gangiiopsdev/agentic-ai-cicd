from fastapi import FastAPI
import ping3

def run_ping(host):
    try:
        response = ping3.ping(host)
        return {'status': 'completed', 'response_time': response}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return run_ping(host)