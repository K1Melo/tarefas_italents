// Cria a array de 3 valores
// Leia os 3 valores
// Crie 2 for loops, que vão percorrer a array, o primeiro vai percorrer a 
// array de forma mais lenta e o segundo vai comparando com o valor do primeiro
// caso o valor na array seja menor, ele vai trocar com o valor que vai ser decidido  
// pela variavel j do for loop
// Escreva a array

programa {
  funcao inicio() {
    inteiro arr[3]

    escreva("Escreva o 1° numero: ")
    leia(arr[0])
    escreva("Escreva o 2° numero: ")
    leia(arr[1])
    escreva("Escreva o 3° numero: ")
    leia(arr[2])

    para(inteiro i = 0; i < 3; i++) {
        para(inteiro j = 0; j < 3; j++) {
          se(arr[i] < arr[j]) {
            inteiro aux = arr[i]
            arr[i] = arr[j]
            arr[j] = aux
          }
        }
    }

    escreva(arr)
  }
}
