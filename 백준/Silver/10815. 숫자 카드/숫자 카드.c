#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b) {
    int n1 = *(int *)a;
    int n2 = *(int *)b;
    return (n1 > n2) - (n1 <  n2);
}

int binary_search(int *arr, int size, int target) {
    int left = 0, right = size - 1;

    while(left <= right) {
        int mid = (left + right) / 2;
        if(arr[mid] == target) return 1;
        else if(arr[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return 0;
}

int main() {
    int N, M;
    scanf("%d", &N);
    int *cards = malloc(N * sizeof(int));
    for(int i=0;i<N;i++) {
        scanf("%d", &cards[i]);
    }

    qsort(cards, N, sizeof(int), compare);

    scanf("%d", &M);
    int *queries = malloc(M * sizeof(int));
    for(int i=0;i<M;i++) {
        scanf("%d", &queries[i]);
    }

    for(int i=0;i<M;i++) {
        printf("%d ", binary_search(cards, N, queries[i]));
    }

    free(cards);
    free(queries);
}