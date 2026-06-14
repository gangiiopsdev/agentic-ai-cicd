from fastapi import FastAPI

def ping(host: str):
    try:
        # Simulating a successful response for demonstration purposes
        return {'status': 'success'}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}