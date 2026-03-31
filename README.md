Autor: Oliver Yoshio Kayano

RA: 1110482613019

Receba 4 notas bimestrais de um aluno. Calcule e mostre a média aritmética. Mostre a mensagem de acordo com a média: a. Se a média for >= 6,0 exibir “APROVADO”; b. Se a média for >= 3,0 ou < 6,0 exibir “EXAME”; c. Se a média for < 3,0 exibir “RETIDO”.

2. Baseado no enunciado, fazer:
   
a. Criar no Linux a pasta /tmp/exercicios

i. Assegurar que ela tem permissão 744 (Fazer em Python)

b. Declarar como globais, as variáveis:

i. nome: str = ‘’
ii. nota1, nota2, nota3, nota4, valor_media  float
iii. dir: str = ‘’
iv. arq: str = ‘’

c. Um procedimento main() que inicie uma variável contador, local e chame 5 vezes o
procedimento entrada;

d. O procedimento entrada, usando os globais nome, nota1, nota2, nota3, nota4 e
valor_media, pede a entrada do nome, das notas, chama uma função med(n1, n2,
n3, n4) que calcula e retorna o valor da média aritmética, exiba em console a média
e, por fim, chame o procedimento cadastro(nm, nt1, nt2, nt3, nt4, vlr_med);

e. A função med, recebe como parâmetros, as 4 notas, inicializa uma variável local
media (float), que recebe o cálculo da média aritmética das notas e será o retorno
da função;

f. O procedimento cadastro, recebe o nome do aluno, as 4 notas e a média como
parâmetros, declara linha, como str e usa arq e dir como globais que devem ter dir
= ‘/tmp/exercicios’ e arq = ‘ex21.txt’ . A variável linha deve receber uma operação de
concatenar de nome, todas as notas e a média, sempre separados por ‘;’ e com
quebra de linha ‘\n’ ao final. As variáveis numéricas, para serem concatenadas,
devem passar por uma operação de cast (str(n1)). Por fim, deve chamar o
procedimento escreveArq(caminho, arquivo, linha_arq).

g. A função escreveArq recebe, como parâmetros, o nome do diretório, o nome do
arquivo e a linha concatenada, para ser gravada no arquivo. Deve declarar file, tipo
e enc como str vazios. Baseado no material de aula, deve-se verificar se o diretório
existe e é diretório e, em sendo verdadeiro, verificar se o arquivo existe (Para definir
se o tipo da operação será w (write) ou a (append))
