## Resumo Resolução do Teste de RPCW 2024
Jéssica Fernandes a93318

### Exercício 1
Comecei por ler a história retirando as palavras chave.
De seguida, li as queries que deveriam ser produzidas para saber que conhecimento deveria poder ser extraído e de que forma.

Tendo o contexto e sabendo que relações seriam necessárias, criei todas as classes relevantes à história que são: Agricultor, TrabalhadorTemporario, Produto e Animal.

Agricultores serão os senhores Carlos e João, que terão um identificador e o seu nome.

Produtos serão as frutas, vegetais e geleias que serão vendidos no mercado. Estes produtos terão um identificador, um nome e um preço.

Animais serão os animais criados pelo senhor Carlos (que terão um identificador e um nome).

Os TrabalhadorTemporario serão os trabalhadores contratados pelo senhor João, que terão também um identificador, um nome e ainda um valor de salário.

Depois de ter a ontologia feita bastou ser importada para o graphdb, onde construí as queries sparql solicitadas.

### Exercício 2
Neste exercício foi nos facultada já a ontologia médica sobre a qual era preciso trabalhar. Foi preciso interpreta-la com cuidado para distinguir as várias classes e relações entre as mesmas, mais uma vez.

Após isto foi criado um `script_doencas.py` para tratar os sintomas e descrições das doenças com os csv `Disease_Syntoms` e `Disease_Description`. Deste script aplicado à ontologia fornecida saiu o `med_doencas.ttl`.

De seguida, foi criado o `script_tratamentos.py` para tratar a parte dos tratamentos com o csv `Disease_Treatment.csv`. A este script foi dado como input o `med_doencas.ttl`, e o seu output é o `med_tratamentos.ttl`.

Finalmente, foi criado o `script_doentes.py` para criar os doentes a partir do json `a93318.json`, resultando o ficheiro `med_doentes.ttl`.

Esta ontologia final foi importada no graphdb para depois serem respondidas as queries solicitadas.