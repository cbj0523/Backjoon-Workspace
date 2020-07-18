#include <stdio.h>
void main() {
    int input, a, b, i;
    scanf("%d", &input);
    for(i = 0; i < input; i++){
        scanf("%d %d", &a, &b);
        printf("%d\n", a+b);
    }
}

// Python으로 풀지 못해 인터넷에서 C언어 예제 가져옴