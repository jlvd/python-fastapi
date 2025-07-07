from fastapi import FastAPI
import uvicorn

## Create the FastAPI app
app = FastAPI()

@app.get("/hola_mundo")
async def saludo():
    return {"message": "Hola, mundo!"}

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 8000
    print(f"🚀 Servidor corriendo en http://{host}:{port}/hola_mundo")
    uvicorn.run("easy-api:app", host=host, port=port, reload=True)