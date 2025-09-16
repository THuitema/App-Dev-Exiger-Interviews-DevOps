"""
To run locally: `fastapi dev main.py`

To run on exec in Docker: `fastapi run main.py --port <port>`
"""

from fastapi import FastAPI

app = FastAPI()

@app.get('/', status_code=200)
def helloWorld():
    return {'message': 'Hello World!'}