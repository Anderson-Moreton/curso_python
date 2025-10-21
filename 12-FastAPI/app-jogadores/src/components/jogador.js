import React from 'react';
import axios from 'axios';

function Jogador(props) {
    const excluiJogador = (jogadorId) => {
        axios.delete(`http://localhost:8000/jogadores/${jogadorId}`)
            .then(
                response => {
                    alert('Jogador excluído com sucesso!');
                }
            )
    }

    return (
        <div>
            <p>
                <span className = 'fw-bold'>
                    {props.jogador.jogador_nome} - {props.jogador.jogador_idade} anos - Time: {props.jogador.jogador_time}
                </span>
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
