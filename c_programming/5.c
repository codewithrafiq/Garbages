#include <stdio.h>

int automorphic(int num)
{

    int square = num * num;

    while (num != 0)
    {
        if (num % 10 != square % 10)
        {
            return 0;
        }

        num /= 10;
        square /= 10;
    }
    return 1;
}

int main()
{
    int num = 0;
    printf("Enter a number: ");
    scanf("%d", &num);
    int square = num * num;

    if (automorphic(num))
    {
        printf("%d^2 = %d\n", num, square);
        printf("%d is an automorphic number\n", num);
    }
    else
    {
        printf("%d^2 = %d\n", num, square);
        printf("%d is not an automorphic number\n", num);
    }
}