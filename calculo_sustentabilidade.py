"""
Global Solution 2026.2 — D8: Soluções em Energias Renováveis e Sustentáveis
Neighborhood Action Dashboard | Jardim Esperança

Calcula uma comparação simplificada entre postes LED convencionais ligados à
rede e postes solares autônomos com LED e sensores de presença.

Dependências: Python 3.10+ (biblioteca padrão).
Execução: python src/calculo_sustentabilidade.py
"""
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARQUIVO_DADOS = ROOT / "dados" / "calculo_viabilidade.json"


def carregar_parametros(caminho):
    with open(caminho, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def calcular(p):
    quantidade = int(p["quantidade_postes"])
    potencia_kw = float(p["potencia_led_w"]) / 1000
    horas = float(p["horas_funcionamento_por_noite"])
    dias = int(p["dias_funcionamento_por_ano"])
    fator_uso = float(p["fator_uso_com_sensor"])
    preco_kwh = float(p["preco_kwh_reais"])
    fator_co2 = float(p["fator_emissao_rede_kg_co2_por_kwh"])

    # Alternativa 1: luminárias ligadas à rede durante todo o período noturno.
    consumo_convencional_por_poste = potencia_kw * horas * dias
    consumo_convencional_total = consumo_convencional_por_poste * quantidade

    # Alternativa 2: LED solar autônomo. O fator de uso representa a média
    # equivalente de potência plena ao combinar intensidade reduzida e PIR.
    consumo_solar_por_poste = potencia_kw * horas * dias * fator_uso
    consumo_solar_total = consumo_solar_por_poste * quantidade

    # A alternativa 2 é considerada off-grid: não compra energia da rede.
    consumo_rede_solar = consumo_convencional_total * (
        1 - float(p["percentual_energia_solar_disponivel"])
    )
    economia_rede_kwh = consumo_convencional_total - consumo_rede_solar
    reducao_demanda_kwh = consumo_convencional_total - consumo_solar_total

    custo_rede_convencional = consumo_convencional_total * preco_kwh
    custo_rede_solar = consumo_rede_solar * preco_kwh
    economia_financeira = custo_rede_convencional - custo_rede_solar

    co2_convencional = consumo_convencional_total * fator_co2
    co2_solar_operacional = consumo_rede_solar * fator_co2
    reducao_co2 = co2_convencional - co2_solar_operacional

    custo_instalacao_convencional = (
        quantidade * float(p["custo_instalacao_convencional_por_poste_reais"])
    )
    custo_instalacao_solar = (
        quantidade * float(p["custo_instalacao_solar_por_poste_reais"])
    )
    investimento_adicional = custo_instalacao_solar - custo_instalacao_convencional
    payback = (
        investimento_adicional / economia_financeira
        if economia_financeira > 0 else None
    )

    return {
        "quantidade_postes": quantidade,
        "consumo_convencional_kwh_ano": consumo_convencional_total,
        "consumo_solar_kwh_ano": consumo_solar_total,
        "consumo_rede_solar_kwh_ano": consumo_rede_solar,
        "economia_rede_kwh_ano": economia_rede_kwh,
        "reducao_demanda_energia_kwh_ano": reducao_demanda_kwh,
        "custo_energia_convencional_reais_ano": custo_rede_convencional,
        "custo_energia_solar_reais_ano": custo_rede_solar,
        "economia_financeira_reais_ano": economia_financeira,
        "emissao_convencional_kg_co2_ano": co2_convencional,
        "emissao_solar_operacional_kg_co2_ano": co2_solar_operacional,
        "reducao_co2_kg_ano": reducao_co2,
        "instalacao_convencional_reais": custo_instalacao_convencional,
        "instalacao_solar_reais": custo_instalacao_solar,
        "investimento_adicional_reais": investimento_adicional,
        "retorno_simples_anos": payback
    }


def imprimir_resultados(r):
    print("=" * 72)
    print("NEIGHBORHOOD ACTION DASHBOARD — VIABILIDADE DA ILUMINAÇÃO SUSTENTÁVEL")
    print("Bairro: Jardim Esperança")
    print("=" * 72)
    print("\n1) COMPARAÇÃO DO CONSUMO ANUAL")
    print(f"   Quantidade de postes: {r['quantidade_postes']}")
    print(f"   Convencional (rede, LED sempre ligado): "
          f"{r['consumo_convencional_kwh_ano']:,.2f} kWh/ano")
    print(f"   Solar (demanda elétrica estimada do LED): "
          f"{r['consumo_solar_kwh_ano']:,.2f} kWh/ano")
    print(f"   Energia comprada da rede no cenário solar: "
          f"{r['consumo_rede_solar_kwh_ano']:,.2f} kWh/ano")
    print(f"   Economia de energia da rede: "
          f"{r['economia_rede_kwh_ano']:,.2f} kWh/ano")
    print(f"   Redução da demanda elétrica pelo uso do sensor: "
          f"{r['reducao_demanda_energia_kwh_ano']:,.2f} kWh/ano")

    print("\n2) ECONOMIA FINANCEIRA")
    print(f"   Conta anual estimada — convencional: "
          f"R$ {r['custo_energia_convencional_reais_ano']:,.2f}")
    print(f"   Conta anual estimada — solar: "
          f"R$ {r['custo_energia_solar_reais_ano']:,.2f}")
    print(f"   Economia anual na energia da rede: "
          f"R$ {r['economia_financeira_reais_ano']:,.2f}")

    print("\n3) IMPACTO AMBIENTAL OPERACIONAL")
    print(f"   Emissões estimadas — convencional: "
          f"{r['emissao_convencional_kg_co2_ano']:,.2f} kg CO2/ano")
    print(f"   Emissões estimadas — solar (eletricidade da rede): "
          f"{r['emissao_solar_operacional_kg_co2_ano']:,.2f} kg CO2/ano")
    print(f"   Redução estimada: {r['reducao_co2_kg_ano']:,.2f} kg CO2/ano")

    print("\n4) INVESTIMENTO E RETORNO SIMPLES")
    print(f"   Instalação convencional: R$ {r['instalacao_convencional_reais']:,.2f}")
    print(f"   Instalação solar: R$ {r['instalacao_solar_reais']:,.2f}")
    print(f"   Investimento adicional: R$ {r['investimento_adicional_reais']:,.2f}")
    if r["retorno_simples_anos"] is None:
        print("   Retorno simples: não calculável com economia anual não positiva.")
    else:
        print(f"   Retorno simples do investimento adicional: "
              f"{r['retorno_simples_anos']:.2f} anos")

    print("\n5) INDICADORES PARA O DASHBOARD")
    print(f"   Energia da rede evitada: {r['economia_rede_kwh_ano']:,.2f} kWh/ano")
    print(f"   Economia financeira: R$ {r['economia_financeira_reais_ano']:,.2f}/ano")
    print(f"   CO2 evitado: {r['reducao_co2_kg_ano']:,.2f} kg/ano")
    print("   Indicadores adicionais recomendados: disponibilidade dos postes (%),")
    print("   nível médio da bateria (%), falhas por mês e tempo médio de reparo.")

    print("\nObservação: estimativas baseadas em parâmetros fictícios. O cálculo de")
    print("CO2 considera apenas emissões operacionais da energia da rede evitada;")
    print("não inclui ciclo de vida de painéis, baterias, transporte ou descarte.")
    print("=" * 72)


if __name__ == "__main__":
    parametros = carregar_parametros(ARQUIVO_DADOS)
    resultados = calcular(parametros)
    imprimir_resultados(resultados)
