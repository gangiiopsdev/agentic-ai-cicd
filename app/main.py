from fastapi import FastAPI
import socketio

app = FastAPI()

def ping(host: str):
    try:
        s = socketio.Client()
        s.connect('http://localhost')
        s.emit('ping', {'host': host})
        response = s.get('/response')
        return {'status': 'completed', 'output': response}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)