#include <iostream>
using namespace std;


int main(){

    int count = 0;
    int i;
    float numbers[5];
    float sum = 0.0;
    float average;

    for(i = 0; i <= 5; i++)
    {
        cout << i + 1 << ". Enter number: ";
        cin >> numbers[i];
        sum += numbers[i];
        count += 1;
    }
    average = sum / count;
    cout << "\nAverage of all " << count << " numbers is: " << average << endl;
    return 0;
    }
