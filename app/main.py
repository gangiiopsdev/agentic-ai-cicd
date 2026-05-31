from fastapi import FastAPI
import ping3
def ping(host):
    return {'status': 'completed', 'output': str(ping3.ping(host)) if ping3.ping(host) is not None else 'failed'}

g = FastAPI()

g.get("/ping")(ping)