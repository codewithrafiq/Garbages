#include <stdio.h>
int main() {
    int n, i, sum = 0;

    printf("Enter a positive Number: ");
    scanf("%d", &n);

    for (i = 1; i <= n; ++i) {
        sum += i;
    }

    printf("Sum = %d \n", sum);
    return 0;
}

