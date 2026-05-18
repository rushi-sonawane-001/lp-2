#include <iostream>
using namespace std;

int main()
{
    int n;

    cout << "Enter number of elements: ";
    cin >> n;

    int a[n];

    // Input array
    cout << "Enter elements: ";
    for(int i = 0; i < n; i++)
        cin >> a[i];

    // Selection Sort
    for(int i = 0; i < n; i++)
    {
        int min = i;

        for(int j = i + 1; j < n; j++)
        {
            if(a[j] < a[min])
                min = j;
        }

        swap(a[i], a[min]);
    }

    // Output sorted array
    cout << "Sorted Array: ";

    for(int i = 0; i < n; i++)
        cout << a[i] << " ";
}