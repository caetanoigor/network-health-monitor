# Network Health Monitor

Uma ferramenta de linha de comando (CLI) leve e modular em Python para diagnóstico rápido de conectividade e integridade de rede local e externa.

O projeto utiliza exclusivamente bibliotecas padrões do Python (`subprocess`, `socket`, `re`, `argparse`), sem necessidade de dependências externas.

---

## Funcionalidades

- **Detecção Automática de Gateway:** Identifica o gateway padrão consultando a tabela de rotas do sistema operacional (`ip route`).
- **Diagnóstico ICMP (Ping):** Calcula perda de pacotes e tempo médio de resposta (RTT) para o gateway local e hosts externos que você definir.
- **Validação de DNS:** Testa a resolução de nomes via chamadas de socket do sistema operacional.
- **Interface CLI com flags:** Permite customizar alvos, domínios e contagem de pacotes através de flags no terminal.

---

## Estrutura do Projeto

```text
network-health-monitor/
├── netmonitor/
│   ├── __init__.py
│   ├── __main__.py      # Ponto de entrada do pacote executável
│   ├── checker.py       # Lógica central de rede (gateway, ping, dns)
│   └── cli.py           # Interface de linha de comando (argparse)
├── requirements.txt
├── setup.sh
├── .gitignore
├── LICENSE
└── README.md

---

## Instalação e Configuração

Clone o repositório e configure o ambiente local:

```bash
# 1. Clonar o repositório
git clone [https://github.com/caetanoigor/network-health-monitor.git](https://github.com/caetanoigor/network-health-monitor.git)
cd network-health-monitor

# 2. Conceder permissão e executar script de setup inicial
chmod +x setup.sh
./setup.sh

# 3. Ativar o ambiente virtual e instalar o CLI em modo editável
source venv/bin/activate
pip install -e .

# 4. (Opcional) Disponibilizar o comando globalmente no sistema sem depender do ambiente virtual venv
mkdir -p ~/.local/bin
ln -s "$(pwd)/venv/bin/netmonitor" ~/.local/bin/netmonitor
```

> **Nota**: Caso execute o utilitário diretamente fora do ambiente virtual, confirme se o diretório `~/.local/bin` está presente na variável `$PATH` da sua sessão (ex.: adicionando `export PATH="$HOME/.local/bin:$PATH"` ao arquivo `~/.bashrc` ou `~/.zshrc` dependendo do shell que você estiver usando).

---

## Como Usar

Após a instalação, o comando `netmonitor` fica disponível para execução direta no terminal:

### Diagnóstico Padrão
Executa a validação padrão (Gateway local, resolução de `google.com` e ping externo em `8.8.8.8` com 4 pacotes):
```bash
netmonitor
```

### Alvos e Parâmetros Customizados
Permite definir destinos específicos, endereços DNS alternativos e a quantidade de pacotes:
```bash
netmonitor -t 1.1.1.1 -d github.com -c 2
```

### Menu de Ajuda
Exibe todas as flags e instruções disponíveis:
```bash
netmonitor --help
```

---

## Parâmetros Disponíveis

| Flag | Parâmetro Longo | Tipo | Padrão | Descrição |
| :--- | :--- | :--- | :--- | :--- |
| `-t` | `--target` | `str` | `8.8.8.8` | Hostname ou IP para teste de conectividade ICMP |
| `-d` | `--dns-test` | `str` | `google.com` | Nome de domínio para teste de resolução DNS |
| `-c` | `--count` | `int` | `4` | Número de pacotes ICMP enviados por execução |
| `-h` | `--help` | - | - | Exibe o menu de ajuda e sai |

---

## Licença

Distribuído sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.
