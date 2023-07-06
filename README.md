<span style="font-size:30px;">〰️Template Method Pattern〰️</span> <br>
O Template Method Pattern é um padrão de design comportamental que permite definir o esqueleto de um algoritmo em uma classe base, enquanto delega a implementação de certos passos desse algoritmo para subclasses. Essa abordagem facilita a reutilização de código e a extensibilidade, permitindo que as subclasses alterem ou estendam partes específicas do algoritmo sem modificar sua estrutura geral.
<br>
Estrutura do Padrão
<br>
O padrão Template Method envolve as seguintes entidades:
<br>
<br>Classe Abstrata: Define o esqueleto do algoritmo em um método chamado templateMethod(). Esse método geralmente é declarado como final <br>para evitar que subclasses o modifiquem. Ele também pode conter outros métodos concretos ou abstratos que são utilizados pelo algoritmo.
<br>
<br>Métodos Concretos: São implementações concretas dos métodos declarados na classe abstrata. Esses métodos são usados pelo <br>templateMethod() ou por outros métodos na classe abstrata.
<br>
<br>Métodos Abstratos: São declarados na classe abstrata, mas não têm implementação. Esses métodos são definidos nas subclasses para fornecer implementações específicas.
<br>
<br>Funcionamento do Padrão
<br>O padrão Template Method permite que a classe base controle o fluxo geral do algoritmo, enquanto permite que subclasses substituam partes específicas do mesmo. O método templateMethod() na classe abstrata geralmente segue uma sequência fixa de etapas que são comuns a todos os algoritmos, mas determinados passos são delegados às subclasses.

<br>Aqui estão as etapas básicas para usar o padrão Template Method:

- Crie uma classe abstrata que defina o esqueleto do algoritmo e declare o método templateMethod(). Identifique partes do algoritmo que podem variar e defina-os como métodos abstratos.

- Implemente os métodos concretos na classe abstrata que são comuns a todas as subclasses e necessários para a execução do algoritmo.

- Crie subclasses que herdem da classe abstrata e forneçam implementações específicas para os métodos abstratos. Essas subclasses podem estender ou substituir partes do algoritmo conforme necessário.

- Utilize o método templateMethod() na classe abstrata para executar o algoritmo completo, aproveitando as implementações fornecidas pelas subclasses para os métodos abstratos.
