tempo=int(input('Digite o tempo da viagem em horas: '))
velocidade=int(input('Digite a velocidade média em Km/h: '))
 
distancia=tempo*velocidade
litros=distancia/12

print(f"total de litros: {litros}")