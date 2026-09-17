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
