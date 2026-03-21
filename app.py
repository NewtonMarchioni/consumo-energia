# Calculadora de Consumo Elétrico Inteligente
# Desenvolvido por Newton Marchioni

print("\n          ***  Calculadora de Consumo Elétrico Inteligente  ***")
print("---------------------------------------------------------------------------------------")   
    
#Entrada
nome = input("\nInforme o tipo de equipamento que deseja calcular o consumo mensal de energia: ").strip().upper()
potencia = int(input("\nInforme a potência em watts (w): "))
horasDia = float(input("\nInforme o tempo médio de uso diário, em horas: "))  
  
#Processamento
consumoMensal = (potencia * horasDia * 30) // 1000
custo = consumoMensal * 0.75

#Saída
print()
print("\n-------------------------------RESULTADO----------------------------------------------")
print(f"\nEquipamento: {nome}")
print(f"Consumo estimado: {consumoMensal:.0f} KWh/mês")
print(f"Considerando a tarifa atual de R$ 0,75 por KWh o custo mensal estimado é de R$ {custo:.2f}")
print("--------------------------------------------------------------------------------------", end="\n\n\n")