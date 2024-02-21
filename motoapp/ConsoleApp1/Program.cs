using ConsoleApp1;

var stack = new BasicStack<double>();
stack.Push(4.5);
stack.Push(6);
stack.Push(8);
var stackString = new BasicStack<string>();
stackString.Push("Company");
double sum = 0.0;

while (stack.Count > 0)
{
    double item = stack.Pop();
    Console.WriteLine(item);
    sum += item;
}
Console.WriteLine(sum);