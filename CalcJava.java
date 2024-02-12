import java.util.Scanner;

public class Calculadora {
    public static void main(String[] args) {

    // Cria um objeto Scanner para ler a entrada do usuário
    Scanner scanner = new Scanner(System.in);

    System.out.println("Escolha a opção: ");
    System.out.println("1: Soma");
    System.out.println("2: Subtração");
    System.out.println("3: Multiplicação");
    System.out.println("4: Divisão");
    // Pergunta ao usuario o tipo de conta que ira fazer armazenando resultado na variavel numC
    System.out.print("");
    double numC = scanner.nextDouble();
    // Verifica se a opção escolhida for maior que 4 sendo assim invalida
    if (numC > 4) {
        System.out.print("Digite uma opção valida");
        System.exit(0);
    }
    // Pergunta o primeiro numero ao usuario armazenando na variavel num1
    System.out.print("Primeiro Numero: ");
    double num1 = scanner.nextDouble();
    // Pergunta o segundo numero ao usuario armazenando na variavel num2
    System.out.print("Segundo Numero: ");
    double num2 = scanner.nextDouble();
    // Variavel onde se armazena o resultado
    double Resultado = 0;

    // Verifica se a opção escolhida foi 1 assim somando o resultado
    if (numC == 1) {
        Resultado = num1 + num2;
        System.out.print(Resultado);
    }
    // Verifica se a opção escolhida foi 2 assim subtraindo o resultado
    if (numC == 2) {
        Resultado = num1 - num2;
        System.out.print(Resultado);
    }
    // Verifica se a opção escolhida foi 3 assim multiplicando o resultado
    if (numC == 3) {
        Resultado = num1 * num2;
        System.out.print(Resultado);
    }
    // Verifica se a opção escolhida foi 4 assim dividindo o resultado
    if (numC == 4) {
        Resultado = num1 / num2;
        System.out.print(Resultado);
    }

    // Não se esqueça de fechar o Scanner quando não for mais necessário
    scanner.close();

    }
}
