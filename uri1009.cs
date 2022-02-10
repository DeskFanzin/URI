using System;
class URI {
    static void Main(string[] args) { 
        string nome;
        double shora, vendas, vendaporc, salario;
        nome = Console.ReadLine();
        shora = double.Parse(Console.ReadLine());
        vendas = double.Parse(Console.ReadLine());
        vendaporc = vendas * 15 / 100;
        salario = shora + vendaporc;
        Console.WriteLine("TOTAL = R$ "+salario.ToString("0.00"));
    }
}
