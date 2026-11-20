# Relatório — Disciplina 08: Soluções em Energias Renováveis e Sustentáveis

**Global Solution 2026.2 — CitizenTech: Da cidade ao campo, tecnologia para a vida cotidiana**  
**Projeto:** Neighborhood Action Dashboard — Jardim Esperança  
**Integrantes:** João Pedro Oliveira da Silva (RM574984) e Arthur Salgado (RM576288)

## 1. Introdução

A iluminação pública contribui para a segurança, a mobilidade e a utilização dos espaços coletivos. No cenário fictício do bairro Jardim Esperança, foram considerados dois problemas: o consumo de energia dos postes convencionais, que permanecem ligados durante toda a noite, e a existência de pontos escuros onde a cobertura de iluminação é insuficiente.

Este trabalho apresenta uma proposta de melhoria sustentável baseada em postes autônomos com energia solar, luminárias LED e sensores conectados ao Neighborhood Action Dashboard. O objetivo é comparar uma solução convencional com uma alternativa renovável, estimar consumo e custos, analisar impactos ambientais e definir indicadores para acompanhamento comunitário.

Os valores utilizados são hipotéticos e foram organizados em `dados/calculo_viabilidade.json`. Eles servem para demonstrar o método de cálculo e não substituem medições locais, especificações técnicas ou cotações comerciais.

## 2. Comparação das Alternativas

### 2.1 Parâmetros adotados

A simulação considera 40 postes, cada um com luminária LED de 30 W, funcionamento durante 12 horas por noite e 365 dias por ano. O preço de energia foi estimado em R$ 0,95/kWh e o fator de emissão da rede em 0,075 kg CO2/kWh.

Para a alternativa com sensores, foi adotado um fator de uso equivalente de 35%. Esse parâmetro representa a combinação entre iluminação em intensidade reduzida quando não há movimento e intensidade maior quando o sensor PIR detecta presença.

### 2.2 Alternativa 1 — LED convencional conectado à rede

O consumo anual é calculado por:

\[
E_1 = N \cdot P \cdot h \cdot d
\]

Onde \(N\) é o número de postes, \(P\) é a potência em kW, \(h\) são as horas diárias e \(d\) são os dias de funcionamento.

\[
E_1=40\cdot0,03\cdot12\cdot365
=5.256\text{ kWh/ano}
\]

O custo anual estimado de energia é:

\[
C_1=5.256\cdot R\$0,95=R\$4.993,20
\]

### 2.3 Alternativa 2 — Poste solar autônomo com LED e sensores

A demanda elétrica equivalente da luminária é estimada por:

\[
E_2=N\cdot P\cdot h\cdot d\cdot f
\]

Em que \(f=0,35\) é o fator de uso médio adotado.

\[
E_2=40\cdot0,03\cdot12\cdot365\cdot0,35
=1.839,60\text{ kWh/ano}
\]

Essa energia é fornecida pelo conjunto fotovoltaico e pela bateria. Considerando o sistema autônomo, sem consumo operacional da rede, a compra de energia da rede para os postes é estimada em zero.

A redução da demanda elétrica equivalente das luminárias é:

\[
\Delta E=5.256-1.839,60=3.416,40\text{ kWh/ano}
\]

A energia evitada na rede é de 5.256 kWh/ano, pois a alternativa solar foi dimensionada como autônoma. A economia financeira estimada na conta de energia é:

\[
\Delta C=5.256\cdot R\$0,95=R\$4.993,20/ano
\]

É importante diferenciar a redução da demanda elétrica das luminárias (3.416,40 kWh/ano) da energia comprada da rede que deixa de ser consumida (5.256 kWh/ano). A energia utilizada pela solução solar continua existindo, mas é fornecida localmente pelo sistema fotovoltaico.

### 2.4 Custos de instalação e viabilidade

Para comparar o investimento inicial, foram adotados custos hipotéticos de R$ 3.500 por poste convencional e R$ 6.500 por poste solar.

| Item | Convencional | Solar autônomo |
|---|---:|---:|
| Custo por poste | R$ 3.500,00 | R$ 6.500,00 |
| Quantidade | 40 | 40 |
| Investimento total | R$ 140.000,00 | R$ 260.000,00 |
| Energia anual comprada da rede | 5.256 kWh | 0 kWh |
| Custo anual de energia | R$ 4.993,20 | R$ 0,00 |

O investimento adicional da alternativa solar é de R$ 120.000,00. Considerando somente a economia anual de energia, o retorno simples é:

\[
T_{retorno}=\frac{120.000}{4.993,20}\approx24,03\text{ anos}
\]

Esse prazo não inclui manutenção, troca de baterias, limpeza dos painéis, conectividade, degradação dos componentes ou custo de capital. Portanto, a viabilidade financeira não deve ser justificada apenas pela economia na conta de energia. A solução também pode ser relevante para instalar iluminação em pontos onde a extensão da rede elétrica seja difícil ou cara, mas essa vantagem exige vistoria e orçamento local.

## 3. Impactos Ambientais

A redução estimada de emissões operacionais é calculada pela energia da rede evitada multiplicada pelo fator de emissão adotado:

\[
CO_2=E_{evitada}\cdot FE
\]

\[
CO_2=5.256\cdot0,075=394,20\text{ kg CO}_2/ano
\]

Assim, a estimativa é de aproximadamente 394,20 kg de CO2 evitados por ano para o conjunto de 40 postes, considerando apenas a eletricidade da rede que deixa de ser consumida.

Esse cálculo não representa uma avaliação completa do ciclo de vida. A fabricação dos painéis, baterias, luminárias e estruturas, o transporte, a substituição e o descarte dos componentes também geram impactos ambientais. Para reduzir esses impactos, recomenda-se utilizar equipamentos duráveis, prever logística reversa e destinação adequada das baterias e componentes eletrônicos.

Entre os benefícios comunitários esperados estão a ampliação da iluminação em pontos escuros, a melhoria da circulação noturna e a possibilidade de acompanhar falhas e disponibilidade dos postes pelo dashboard.

## 4. Indicadores de Eficiência e Sustentabilidade

Os seguintes indicadores podem ser apresentados no Neighborhood Action Dashboard:

| Indicador | Forma de cálculo ou coleta | Meta/Referência inicial |
|---|---|---|
| Energia da rede evitada | Consumo convencional estimado menos consumo da rede no sistema solar | 5.256 kWh/ano |
| Redução da demanda das luminárias | Consumo convencional menos demanda equivalente com sensores | 3.416,40 kWh/ano |
| Economia financeira | kWh da rede evitados × tarifa | R$ 4.993,20/ano |
| CO2 operacional evitado | kWh da rede evitados × fator de emissão | 394,20 kg/ano |
| Disponibilidade dos postes | Horas em funcionamento ÷ horas previstas × 100 | Meta proposta: ≥ 98% |
| Estado da bateria | Percentual de carga informado pelo controlador | Monitoramento contínuo |
| Falhas por mês | Contagem de alertas de falha por período | Redução ao longo do tempo |
| Tempo médio de reparo | Soma do tempo entre alerta e correção ÷ falhas atendidas | Acompanhar mensalmente |

As metas de disponibilidade são propostas iniciais e devem ser ajustadas após um período de teste. Os indicadores de consumo e CO2 também devem ser recalculados com medições reais de energia, tarifa e fator de emissão aplicável ao período.

### 4.1 Esquema conceitual de funcionamento

O diagrama completo está no arquivo `diagramas/esquema_conceitual.md`. O fluxo básico é:

1. **Fonte:** Sol → placa fotovoltaica → controlador de carga → bateria.
2. **Sensores:** LDR identifica o escuro; PIR identifica movimento.
3. **Lógica:** microcontrolador decide o nível de iluminação e registra o estado do sistema.
4. **Comunicação:** dados são enviados pela rede disponível, com armazenamento local em caso de falha de conexão.
5. **Dashboard:** apresenta economia estimada, energia, bateria, disponibilidade e alertas de manutenção.

O controle local deve continuar funcionando sem conexão com a internet. O painel serve para monitoramento e apoio à manutenção, não como requisito para o poste acender.

## 5. Conclusão

A proposta de postes autônomos solares com LED e sensores apresenta uma alternativa para reduzir a dependência da rede elétrica e ampliar a iluminação em áreas prioritárias do Jardim Esperança. Na simulação com 40 postes, a solução convencional consumiria 5.256 kWh por ano, enquanto a demanda equivalente estimada da solução com sensores seria de 1.839,60 kWh por ano, fornecida por energia solar.

A economia estimada na energia comprada da rede é de R$ 4.993,20 por ano, e a redução de emissões operacionais é de aproximadamente 394,20 kg de CO2 por ano. Entretanto, o investimento inicial solar é maior e o retorno simples estimado, considerando somente a conta de energia, é de aproximadamente 24 anos. Isso demonstra que a decisão deve considerar também a dificuldade de levar a rede elétrica a determinados pontos, os benefícios sociais, a manutenção e a vida útil das baterias.

Conclui-se que a proposta tem potencial ambiental e comunitário, desde que seja precedida por estudo técnico de dimensionamento, análise dos locais, consulta aos moradores e planejamento de manutenção e descarte. O Neighborhood Action Dashboard complementa a solução ao transformar dados de funcionamento em indicadores compreensíveis e alertas que apoiam decisões sobre onde e quando agir.
