import React from 'react';
import axios from 'axios';

function Jogador(props) {
    const excluiJogador = (jogadorId) => {
        axios.delete(`http://localhost:8000/jogadores/${jogadorId}`)
            .then(
                response => {
                    alert("Jogador excluído com sucesso!" + response.data);
                }
            )
    }
    const editaJogador = (jogador) => {
        props.setJogadorId(jogador.id);
        props.setJogadorNome(jogador.nome);
        props.setJogadorIdade(jogador.idade);
        props.setJogadorTime(jogador.time);
        props.setBotaoTexto('Atualizar');
    }

    return (
        <div>
            <p>
                <span className = 'fw-bold'>
                    {props.jogador.jogador_nome} - {props.jogador.jogador_idade} anos - Time: {props.jogador.jogador_time}
                </span>
                <button
                    onClick={() => editaJogador(props.jogador)}
                    className = 'btn btn-danger'
                >
                    <span className = 'badge rounded-pill bg-info'>Editar</span>
                </button>
                <button 
                    onClick={() => excluiJogador(props.jogador.jogador_id)}
                    className = 'btn btn-danger'
                >
                    <span className = 'badge rounded-pill bg-danger'>X</span>
                </button>
            </p>
        </div>
    );
}

export default Jogador;
