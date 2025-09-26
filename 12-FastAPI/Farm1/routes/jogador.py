from fastapi import APIRouter
from config.database import conexao
from models.jogador import Jogador
from schemas.jogador import jogadoresEntidade, listaJogadoresEntidade
from bson import ObjectId


jogador_router = APIRouter()

@jogador_router.get('/')
async def inicio():
    return "Welcome to FullStack Farm"

#Lista todos os jogadores
@jogador_router.get('/jogadores')
async def lista_jogadores():
    return listaJogadoresEntidade(conexao.local.jogador.find())

#Detalher de um jogador
@jogador_router.get('/jogadores/{jogador_id}')
def busca_jogador_id(jogador_id):
    return jogadoresEntidade(
        conexao.local.jogador.find_one
        (
            {"_id": ObjectId(jogador_id)}
        )
    )

# Insere novos Jogadores
@jogador_router.post('/jogadores')
async def cadastra_jogadores(jogador: Jogador):
    conexao.local.jogador.insert_one(dict(jogador))
    return listaJogadoresEntidade(conexao.local.jogador.find())

#Atualiza jogadro
@jogador_router.put('/jogadores/{jogador_id}')
async def atualiza_jogador(jogador_id, jogador: Jogador):
    conexao.local.jogador.find_one_and_update(
        {
            "_id": ObjectId(jogador_id)
        },
        {
            "$set": dict(jogador)
        }
    )
    return jogadoresEntidade(
        conexao.local.jogador.find_one(
            {"_id": ObjectId(jogador_id)}
        )
    )
