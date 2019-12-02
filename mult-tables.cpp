#include <iostream>
using namespace std;

int main() {
    int a;
    int b;


    for(int a=1; a<=10; a++)
        for(int b=1; b<=10; b++) {
            int c = a * b;
            cout<<a<<" "<<"*"<<" "<<b<<" "<<"="<<" "<<c<<endl;
        }
    return 0;

}
