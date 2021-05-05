from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from utils import train_requests

from models.station import get_stations_from_response
from models.departure import get_departures_from_response

app = FastAPI()

maquinas = {
	"1": {
  	"name": "Cortadora",
    "status": "rodando",
  },
  "2": {
    "name": "Fresa",
    "status": "erro",
  },
}

DEFAULT_ERROR = {
    "name": "Cortador a Laser",
    "status": "parada",
},

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/departures/{id_maquina}")
def get_departures(id_maquina: str):
    return maquinas.get(id_maquina, DEFAULT_ERROR)