import { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import JogadorList from './components/jogadorList';

function App() {

  const [jogadorList, setJogadorList] = useState([]);
  const [jogadorNome, setJogadorNome] = useState('');
  const [jogadorIdade, setJogadorIdade] = useState('');
  const [jogadorTime, setJogadorTime] = useState('');
  const [jogadorId, setJogadorId] = useState('');
  const [botaoTexto, setBotaoTexto] = useState('Cadastrar');

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/jogadores')
      .then(response => {
        console.log(response.data)
        setJogadorList(response.data)
      }).catch(
        (error) => {console.log(error)}
      )
  });

  const adicionaJogador = (jogador) => {
    axios.post('http://127.0.0.1:8000/jogadores', jogador)
      .then((response) => {
        setJogadorList([...jogadorList, response.data]);
      }).catch((error) => {
        console.error('Erro ao adicionar jogador:', error);
      });
  };

  const atualizaJogador = (jogador) => {
    axios.put(`http://127.0.0.1:8000/jogadores/${jogadorId}`, jogador)
      .then(response =>{
        alert("Jogador atualizado com sucesso!" + response.data);
      })
      .catch((error) => {
        console.error('Erro ao atualizar jogador:', error);
      })
  }

  const adicionaAtualizaJogador = () =>{
    const jogador = {
      'jogador_nome' : jogadorNome,
      'jogador_idade' : jogadorIdade,
      'jogador_time' : jogadorTime
    }

    if(jogadorId !== ''){
      atualizaJogador(jogador);
    } else{
      adicionaJogador(jogador);
    }

  }

  return (
    <div className='container'>
      <div 
       className='mt-3 justify-content-center align-items-center mx-auto'
       style={{ "maxWidth": "60vw", "backgroundColor": "#ffffff" }}
      >
        <h2 className = 'text-center text-white bg-success card mb-1'>Gerenciamento de Jogadores</h2>
        <h6 className = 'card text-center text-white bg-success mb-2 pb-2'>Informações dos jogadores</h6>
        <div className = 'card-body text-center'>
          <h5 className = 'card text-center text-white bg-dark mb-2 pb-1'>Cadastro de jogadores</h5>
          <span className = 'card-text'>
            <input
              onChange={ Event => setJogadorNome(Event.target.value) }
              value={jogadorNome}
              className = 'mb-2 form-control' placeholder='Informe o Nome'
            />
            <input
              onChange={ Event => setJogadorIdade(Event.target.value) } 
              value={jogadorIdade}
              className = 'mb-2 form-control' placeholder='Informe a Idade'
            />
            <input
              onChange={ Event => setJogadorTime(Event.target.value) }
              value={jogadorTime}
              className= 'mb-2 form-control' placeholder='Informe o Time'
            />
            <button 
              onClick={adicionaAtualizaJogador}
              className ='btn btn-outline-success mb-4'>
              {botaoTexto}
            </button>
          </span>
          <h5 className = 'card text-center text-white bg-dark mb-3 pb-1'>Lista de Jogadores</h5>
          <div>
            <JogadorList 
              jogadorList={jogadorList}
              setJogadorId={setJogadorId}
              setJogadorNome={setJogadorNome}
              setJogadorIdade={setJogadorIdade}
              setJogadorTime={setJogadorTime}
              setBotaoTexto={setBotaoTexto}
            />
          </div>
        </div>
        <h6 className = 'card text-center text-light bg-success py-1'>Anderson Moreton - 2025</h6>
      </div>
    </div>
  );
}

export default App;
