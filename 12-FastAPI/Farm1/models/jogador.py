from pydantic import BaseModel

class Jogador(BaseModel):
    jogador_nome: str
    Jogador_idade: int
    jogador_time: str

