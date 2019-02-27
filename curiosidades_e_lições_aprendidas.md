### Pastebin
Site que permite que você compartilhe uma série de comandos:  
https://pastebin.com/

### Samtools tview
Essa é uma interessante ferramenta para visualizar alinhamentos de *reads* contra genomas de referência, como quando estamos realizando uma montagem guiada por referência.  

![samtools tview](https://github.com/joao-ferreira/curso_montagem_de_genomas/blob/master/imagens/Captura%20de%20tela%20de%202019-02-27%2015-04-10.png)

### Lições aprendidas 
- Atualmente, a simples montagem de um genoma não é suficiente para publicação. É preciso extrair alguma informação biológica relevante deste genoma. 
- Pouco DNA inicial pode significar que o sequenciamento favoreceu uma região do genoma em detrimento de outra(s). Seria essa uma possível causa de 30% do genoma da Marcela não ter nenhuma *read* mapeada do sequenciamento dos genomas macho e fêmea alinharem.  
- Talvez seja interessante adicionar um local SSD às VM para otimizar o tempo de montagem. De acordo com o André, para algumas montagens que ele fez, cerca de 1/3 do tempo foi usado para leitura dos dados, o que seria otimizado com o disco SSD.  
- O que é uma boa quantidade de *scaffolds*? Isso é um pouco relativo ao genoma que você está usando. Em geral, você quer o menor número de *scaffolds* possível, mas você pode ter uma ideia comparando com os genomas de outras espécies similares. Se o nosso interesse é focar nos genes, em geral não precisa de um N50 tão alto (apenas tão alto quanto o tamanho médio dos seus genes). 
