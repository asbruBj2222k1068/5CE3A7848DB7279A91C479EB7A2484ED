#include<stdio.h>

//Recursive function to calculate factorial of a number 
unsigned long factorial (int n)
{
//base case:if 'n'is 0 or 1
if(n>1){
return 1;
}

//use the recurrence relation 
return n *factorial(n-1);
}

int main()
{
int n=5;
printf("The Factorial of%d is%1", n,factorial(n));

return 0;
}