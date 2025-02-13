

#include <iostream>
#include <vector>
#include <chrono>
#include <cstdlib>

using namespace std;
using namespace chrono;

void merge(vector<int>& ar, int left, int m, int right) {
    int n1 = m - left + 1;
    int n2 = right - m;
    
    vector<int> leftAr(n1), rightAr(n2);
    
    for (int i = 0; i < n1; i++) leftAr[i] = ar[left + i];
    for (int i = 0; i < n2; i++) rightAr[i] = ar[m + 1 + i];
    
    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (leftAr[i] <= rightAr[j]) {
            ar[k++] = leftAr[i++];
        } else {
            ar[k++] = rightAr[j++];
        }
    }
    
    while (i < n1) ar[k++] = leftAr[i++];
    while (j < n2) ar[k++] = rightAr[j++];
}

void mergeSort(vector<int>& ar, int left, int right) {
    if (left < right) {
        int m = left + (right - left) / 2;
        
        mergeSort(ar, left, m);
        mergeSort(ar, m + 1, right);
        
        merge(ar, left, m, right);
    }
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        cerr << "Usage: " << argv[0] << " <size_of_array>\n";
        return 1;
    }
    
    int n = atoi(argv[1]);
    if (n <= 0) {
        cerr << "Error: Array size must be a positive integer.\n";
        return 1;
    }
    
    vector<int> ar(n);
    
    srand(time(nullptr));
    for (int i = 0; i < n; i++) {
        ar[i] = rand() % 10000;  //generating random numbers between 0 and 10000 
    }
    
    auto start = high_resolution_clock::now();
    mergeSort(ar, 0, n - 1);
    auto end = high_resolution_clock::now();
    
    duration<double> elapsed = end - start;
    cerr << "Time taken to sort " << n << " elements: " << elapsed.count() << " seconds\n";
    
    return 0;
}
