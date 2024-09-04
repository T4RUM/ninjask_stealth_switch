# Ninjask_Stealth_Switch [![Ninjask](https://img.pokemondb.net/sprites/black-white/anim/normal/ninjask.gif)](https://pokemondb.net/pokedex/ninjask)

## Descrição
O **Ninjask_Stealth_Switch** é uma ferramenta desenvolvida para facilitar a troca automatizada de endereço IP durante o processo de Pentest. Durante a realização de testes de segurança em um site alvo, é comum que o endereço IP do atacante seja bloqueado em determinadas situações, o que prejudica o progresso do Pentest. Para evitar interrupções manuais e agilizar o processo, o script foi criado para monitorar as respostas do site alvo. Sempre que um status code diferente de 200 é recebido, o script aciona a troca de IP automaticamente, garantindo a continuidade dos testes sem interrupções. Com essa abordagem automatizada, o **Ninjask_Stealth_Switch** permite que o Pentest seja executado de forma mais eficiente, mantendo a privacidade do atacante e contornando bloqueios de IP.

## Funcionalidades
- **Troca Automática de IP:** Troca o endereço IP automaticamente quando um status code diferente de 200 é recebido.
- **Monitoramento de Respostas:** Monitora as respostas do site alvo em tempo real.
- **Continuidade dos Testes:** Garante a continuidade dos testes de Pentest sem interrupções manuais.
- **Privacidade:** Mantém a privacidade do atacante contornando bloqueios de IP.

## Requisitos
- Python 3.x
- NordVPN instalado
- Bibliotecas Python: requests

## Instalação
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu_usuario/Ninjask_Stealth_Switch.git
   cd Ninjask_Stealth_Switch

2. Instale as dependências:
```bash
pip install requests
```

## Configuração
1. Instale o NordVPN e configure-o conforme necessário.
2. Verifique se o NordVPN está configurado para permitir comandos de linha de comando.

## Uso
1. Edite o script para definir a URL do site alvo:
```bash
url = "https://example.com.br/"
```
2. Execute o script:
```bash
python ninjask_stealth_switch.py
```


