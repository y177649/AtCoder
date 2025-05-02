// This is file 86

string[] input_number = Console.ReadLine().Split();

int number_a = int.Parse(input_number[0]);
int number_b = int.Parse(input_number[1]);

int result = number_a * number_b;

//Console.WriteLine(result);

if (result % 2 == 0)
{
    Console.WriteLine("Even");
}
else
{
    Console.WriteLine("Odd");
}
