#include <stdio.h>

int replace(long int number)
{
    if (number == 0)
        return 0;
    int digit = number % 10;
    if (digit == 0)
        digit = 1;
    return replace(number / 10) * 10 + digit;
}
int Convert(long int number)
{
    if (number == 0)
        return 1;
    else
        return replace(number);
}
int main()
{
    long int number;
    printf("\nEnter any number : ");
    scanf("%d", &number);
    printf("\nAfter replacement the number is : %d \n", Convert(number));
    return 0;
}