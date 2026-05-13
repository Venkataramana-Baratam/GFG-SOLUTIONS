// User function template for C
int arraySum(int arr[], int size) {
    int counter = 0;

    for (int i = 0; i < size; i++) {
        counter += arr[i];
    }

    return counter;
}