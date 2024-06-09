# Projeto do Jogo Termo

## 📒 Descrição:
  Esse código foi elaborado para simular o back-end do jogo [Termo](https://term.ooo).
  O código consiste em um jogo de adivinhação de uma palavra que contém 5 letras, as quais precisam ser adivinhadas em 10 tentativas
  com as seguintes regras:
  - Uma palavra de 5 letras será escolhida aleatóriamente do banco de dados fornecidos => [texto.txt](https://github.com/VitorBriosp/Projeto-Jogo-Termo/blob/main/codigo-do-projeto/texto.txt);
  - O usuário irá inserir uma palavra de 5 letras, caso a palavra não se encaixe à regra, um erro será gerado pedindo para o usuário fornecer uma resposta válida;
  - Caso a palavra esteja correta, uma mensagem irá surgir parabenizando o usuário e falando em quantas tentativas ele acertou a resposta;
  - Caso a palavra contenha 5 letras, cada letra será comparada com a palavra secreta;
  - Caso a letra esteja presente na palavra e na posição correta, será informada ao usuário. Exemplo => "palavra secreta: 'CARRO'; palavra informada pelo usuário: 'BRAVO'" a letra O será correta na posição correta, já a Letra R e A serão corretas
    nas posições erradas e por fim as letra B e V estarão erradas, pois não pertencem à palavra secreta;
  - Caso se exceda as 10 tentativas, uma mensagem irá informar ao usuário que suas tentativas se esgotaram, informando a resposta correta e encerrando o jogo.

## 💻 Processo De Desenvolvimento:
  Usei o [Visual Studio Code](https://code.visualstudio.com) como ferramenta de edição de texto e a linguagem [python](https://www.python.org) para desenvolver o código
  do jogo, criei também um arquivo txt e pedi para o ChatGpt 4.0 gerar algumas dezenas de palavras para colocar no banco de dados. Usei também apenas o módulo random para escolher aleatóriamente
  uma das palavras no banco de dados. 

## 💼 Detalhes:
  - Como pode ver no [código](https://github.com/VitorBriosp/Projeto-Jogo-Termo/blob/main/codigo-do-projeto/codpython.py) a formatação que usei em alguns prints pode ser vista como antiquada ou talvez pudesse ser mais simplificada usando o modelo de formatação mais recente, bem, para me desafiar um pouco eu optei por escrever o código
  respeitando a linguagem 3.4 do python, ou seja, sem formatação usando f'';
  - É possível também completar ainda mais o código desenvolvendo um front-end básico em pouco tempo, basta implementar o microframework "Flaks" juntamente com o uso de html e css para estilizar o código à gosto;
  - Como meu objetivo foi desenvolver o back-end do projeto eu optei por não seguir mais adiante.

## ☹️ Final:
- Segue aqui o vídeo de execução do projeto:

https://github.com/VitorBriosp/Projeto-Jogo-Termo/assets/167243828/2c3be4d4-b539-4e03-bb45-393ef3ff096d

