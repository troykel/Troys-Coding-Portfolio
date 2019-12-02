#include <iostream>
using namespace std;

int main()
{
int row0 = 15;
int row1 = 15;
int row2 = 15;
int col0 = 15;
int col1 = 15;
int col2 = 15;
int dia1 = 15;
int dia2 = 15;

if (row0 == row1 && row1 == row2 && row2 == col0 && col0 == col1
        && col1 == col2 && col2 == dia1 && dia1 == dia2) {
        cout << "We have a magic square!" << endl;
        }
        else {
            cout << "All rows,cols,diagonals not equal.  No magic square!" << endl;
        }
        return 0;

}

