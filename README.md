# Global Solution 2026.2 — D8: Soluções em Energias Renováveis e Sustentáveis

## Integrantes
- João Pedro Oliveira da Silva — RM574984
- Arthur Salgado — RM576288

## Descrição do Problema
No cenário fictício **Neighborhood Action Dashboard**, aplicado ao bairro Jardim Esperança, foram identificados dois desafios relacionados à iluminação pública: o consumo de energia dos postes convencionais, que permanecem ligados durante toda a noite, e a existência de pontos escuros onde ainda faltam postes. A proposta busca reduzir o consumo da rede elétrica e ampliar a cobertura de iluminação em locais prioritários, sem comprometer a segurança e a acessibilidade dos moradores.

Os parâmetros utilizados nesta entrega são simulados para fins acadêmicos. Não representam levantamento de campo, orçamento oficial ou medição de consumo real.

## Proposta Sustentável
A proposta é instalar **postes autônomos de iluminação pública com placa fotovoltaica, bateria, luminária LED e sensores IoT**. Durante o dia, a placa solar carrega a bateria. À noite, um sensor LDR identifica a ausência de luz natural e habilita a iluminação. Um sensor PIR detecta movimento: o LED opera em intensidade reduzida quando não há presença e aumenta a intensidade quando pedestres ou veículos são detectados.

Um microcontrolador gerencia o funcionamento local e envia informações de consumo estimado, nível da bateria e falhas para o Neighborhood Action Dashboard. A automação local continua funcionando mesmo quando a comunicação com o painel estiver indisponível.

### Alternativas comparadas
1. **Convencional:** poste LED conectado à rede elétrica, ligado durante 12 horas por noite.
2. **Sustentável:** poste LED alimentado por painel solar e bateria, com controle por LDR e PIR. O fator de uso de 35% representa a potência média equivalente após a dimerização e o acionamento por presença.

A comparação considera 40 postes, LED de 30 W, 365 dias por ano e os demais parâmetros do arquivo JSON. O script calcula consumo anual, energia da rede evitada, economia financeira, emissões operacionais evitadas e retorno simples do investimento adicional.

## Como Executar

1. Instale Python 3.10 ou superior.
2. Abra um terminal na pasta `d8_energias_renovaveis`.
3. Execute:
   ```bash
   python src/calculo_sustentabilidade.py
   ```
4. O script lê `dados/calculo_viabilidade.json` e apresenta os resultados no terminal.

O programa utiliza apenas bibliotecas da instalação padrão do Python (`json` e `pathlib`), portanto não exige instalação de pacotes externos.

## Estrutura de Pastas

```text
d8_energias_renovaveis/
├── dados/
│   └── calculo_viabilidade.json
├── diagramas/
│   └── esquema_conceitual.md
├── src/
│   └── calculo_sustentabilidade.py
├── relatorio_d8.md
└── README.md
```

## Observações sobre a Viabilidade
A economia financeira calculada considera somente a energia comprada da rede que deixa de ser consumida. Não inclui manutenção, troca de baterias, limpeza dos painéis, conectividade, degradação dos equipamentos, custo de capital ou valor social da ampliação da iluminação. O retorno simples deve, portanto, ser interpretado como uma estimativa inicial, não como estudo financeiro definitivo.

A implantação deve ser precedida por vistoria dos locais, estudo de sombreamento, dimensionamento de painéis e baterias para períodos nublados, verificação da cobertura de comunicação e consulta aos moradores. A intensidade reduzida da iluminação deve respeitar requisitos técnicos de segurança, visibilidade e acessibilidade.
