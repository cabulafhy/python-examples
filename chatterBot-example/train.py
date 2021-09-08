from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatBot = ChatBot("meuBot")
trainer = ListTrainer(chatBot)

trainer.train([
    "oi", "olá, tudo bem com você?",
    "oi", "Opa, tudo bom ?",
    "oi", "Oi, tranquilo esquilo ?",
    "oi", "OOOO zé, bão memo ?",
    "você poderia me ajudar", "Claro, qual sua dúvida?",
    "você poderia me ajudar", "Sim, só me diga qual sua dúvida",
    "você poderia me ajudar", "Claro, pode perguntar",
    "você poderia me ajudar", "Sim, pode me perguntar",
    "você sabe programar ?","Sim, sou especialista",
    "você sabe programar ?","Claro, fui criado para isso",
    "você sabe programar ?","Programar é a minha especialidade",
    "você sabe programar ?","Claro, eu já nasci programando",
    "Qual a definição de uma variavel ?", "Basicamente é um recipiente que armazena um valor variavel",
    "Qual a definição de uma variavel ?", "Um recipiente onde é armazenado um valor que pode variar com o tempo",
    "Qual a definição de uma variavel ?", "Váriaveis são uma maneira de armazenar valores em recipiente que pode variar o valor com o tempo",
    "Qual a definição de uma variavel ?", "São campos onde se podem armazenar valores variaveis",
    "Qual a diferença entre variavel e constante?","Uma variavel pode trocar de valor a qualquer momento, uma constante tem um valor fixo",
    "Qual a diferença entre variavel e constante?","Uma constante tem um valor definido fixo, já uma variavel possui a capacidade de mudar de valor",
    "Qual a diferença entre variavel e constante?","Uma variavel realiza trocas de valores, já uma constante não pode fazer essa proeza",
    "Qual a diferença entre variavel e constante?","Uma constante não realiza troca de valores, já uma variavel pode trocar de valores a qualquer momento",
    "O que são arrays ?","Arrays são coleções de dados organizados em uma estrutura de chave e valor",
    "O que são arrays ?","Pode ser organizado em uma estrutura de lista, onde os campos possuem uma chave e um valor correspondente a esta chave",
    "O que são arrays ?","É uma estrutura de dados organizada de forma que possui uma chave e um valor correspondente a esta chave",
    "O que é um loop na programação ?","Loop é uma estrutura de laço de repetição, onde uma determinada ação é repetida determinadas vezes de acordo com uma condição pré estabelecida",
    "O que é um loop na programação ?","Loop se refere as estruturas de repetição da programação. O loop será executado enquanto uma condição dada for verdadeira",
    "O que é um loop na programação ?","É uma estrutura de dados, um laço de repetição. Esse laço é estabelecido em cima de uma condição, e enquato a condição for satisfeita um código será executado",
    "O que é um script?","Script é um código que pode ser interpretado para uma linguagem de maquina",
    "O que é um script?","É uma sequencia de instruções organizadas de forma a fazer sentido dentro de um contexto",
    "O que é um operador ?","Na programação existem vários operadores, eles fazem comparações entre valores e calculos, atribuindo verdadeiro ou falso se os valores passarem nos testes feitos.",
    "O que é um operador ?","São auxiliares na programação, onde fazem calculos e comparações entre valores"    
])