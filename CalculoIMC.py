NOME = str(input('DIGA SEU NOME PARA MIM:'))

SEXO = float(input('Qual é o seu gênero sexual?' 
'\n 1 p/ Homem, 2 p/ Mulher, 3 p/ outro:'))

ALTURA = float(input('Qual é sua altura em centimetros?:'))

PESO =  float(input('Qual é o seu peso?, sem mentir heim:'))

IMC= PESO//(ALTURA/100)**2

if IMC < 18.5:
  print(f'Caracas tá só a capa do Batman heim, imc de {IMC}, é muito abaixo do peso.')
elif IMC >=18.5 and IMC<=24.9:
    print(f'Aí sim, tá de boa, imc de {IMC}, é tipo peso normal.')
elif IMC >=25 and IMC <=29.9:
    n_3=(f'Já tem uns pneuzinhos aí heim, imc de {IMC} é sobrepeso, bora fechar a boca.')
    print(n_3)
elif IMC >=30 and IMC <=34.9:
  print(f'Certeza que sua calça não está fechando rs, imc de {IMC}, isso é obesidade grau 1, cuidado! Mas, que tal, ao invés de renovar o guarda-roupas... Bora malhar!!!')
elif IMC >=35 and IMC <=39.9:
  print(f'Mano do céu!!! , imc de {IMC}, Fecha a boca e vai treinar! Obesidade grau 2.')
elif IMC >=40:
  print(f'imc de {IMC}, atitudes drasticas precisam ser tomadas na sua vida. Treino, dieta, fé... e parar e comer tanto assim também né meu Donuts recheado.')
if SEXO == 2:
    print('OBS.:'
    '\n BORA MULHER, VAI FAZER UNS AGACHAMENTOS E DEPOIS VOLTA AQUI PARA GENTE CONVERSAR...TODA FITNESS HEIM! BLZ ;-)')
elif SEXO ==1:
           print('OBS.:' 
          '\n TE ANIMA HOMI! VAI LEVANTAR UNS FERROS E DEPOIS VOLTA AQUI PARA GENTE CONVERSAR... BLZ!!!')
else:
  print('OBS.:'
  '\n Amor prazer em te conhecer, vamos juntxs nessa caminhada fitness heim meu amore! TMJX')
print('Te espero aqui de volta heim '+NOME, "!!!")