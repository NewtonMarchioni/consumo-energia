⚙️ Calculadora de Consumo Elétrico Inteligente 

🧿 Objetivo: calcular o consumo mensal de energia de aparelhos elétricos 💡

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

Este projeto, em Python, foi criado para praticar o ciclo **Entrada → Processamento → Saída**

🀄 O programa solicita o tipo de aparelho, informações sobre a potência e o tempo de uso diário. Executa o cálculo de consumo e apresenta o resultado. Complementa com o custo estimado mensal.

📌 Foram incluídos dois novos comandos para o resultado ser apresentado em caixa alta .upper() e eliminação de espaços indesejáveis .strip().

👾 Fórmulas para os cálculos:
1. Cálculo do consumo mensal em KWh | consumoMensal = (potencia * horasDia * 30) // 1000
2. Cálculo do custo mensal estimado | custo = consumoMensal * 0.75 

📋 Instruções:
1. Informe o nome do equipamento (texto);
2. Informe a potência em Watts (número);
3. Informe o tempo médio de uso diário (float).