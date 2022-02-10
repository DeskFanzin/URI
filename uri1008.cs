using System;
class URI {
    static void Main(string[] args) { 
        int num, horas;
        float shora, salario;
        num = int.Parse(Console.ReadLine());
        horas = int.Parse(Console.ReadLine());
        shora = float.Parse(Console.ReadLine());
        salario = horas * shora;
        Console.WriteLine("NUMBER = "+num);
        Console.WriteLine("SALARY = U$ "+salario.ToString("0.00"));
    }
}
