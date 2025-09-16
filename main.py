"""
To run locally: `fastapi dev main.py`
To run in docker exec: `
"""

from fastapi import FastAPI

app = FastAPI()

@app.get('/', status_code=200)
def helloWorld():
    return {'message': 'Hello World!'}