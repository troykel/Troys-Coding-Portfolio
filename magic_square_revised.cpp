#include <iostream>
#include <cstdlib>
#include <ctime>
#include <bits/stdc++.h>

using namespace std;


//int randomfunc(int k) {
    //return rand() % k;
//}


int main() {


    int i;
    int j;

    int row0;
    int row1;
    int row2;

    int col0;
    int col1;
    int col2;

    int dia1;
    int dia2;


    int tries = 0;
    while(true){
        tries +=1;
        srand(unsigned(time(0)));

        vector<int> v;

    // set some values from 1-9:
        for (int k = 1; k < 10; ++k)
            v.push_back(k);
    //Using built-in random generator
            random_shuffle(v.begin(), v.end());
    //Using randomfunc
            //random_shuffle(v.begin(), v.end(), randomfunc);

    //Print out the vector's content
    cout << "Randomized vector contains:";
        for (vector<int>::iterator i = v.begin(); i != v.end(); ++i)
            cout << ' ' << *i;

    int troysArray[3][3];
    for (int i = 0;i < 3;i++)
        for (int j = 0;j <3;j++)
    //This is the line which treats the 1d vector like a 2d array.
    //Specifically, the i*3, which converts the rows to 3 at a time.
        troysArray[i][j] = v[i*3 + j];

    cout << endl;

    if (row0 == row1 && row1 == row2 && row2 == col0 && col0 == col1
        && col1 == col2 && col2 == dia1 && dia1 == dia2)
            {
            cout << "We have a magic square!" << endl;
            cout << "Magic Square found after " << tries << " tries" << endl;
            cout << troysArray[3][3] << endl;
            break;
            }
    else {
        cout << "No magic square! All rows,cols,diags are not equal!" << endl;
        cout << "So far " << tries << " tries!" << endl;
        cout << endl;
    }

//}
    // cout << endl;
    // cout << "\n";
//}

    //Ad up row 0 (top row):
    row0 = troysArray[0][0] + troysArray[0][1] + troysArray[0][2];
    cout << "The sum of row 0 equals: " << row0 << endl;

    //Adding up row 1 (middle row):
    row1 = troysArray[1][0] + troysArray[1][1] + troysArray[1][2];
    cout << "The sum of row 1 equals: " << row1 << endl;

    //Adding up row 2 (bottom row):
    row2 = troysArray[2][0] + troysArray[2][1] + troysArray[2][2];
    cout << "The sum of row 2 equals: " << row2 << endl;

    cout << "\n";

    //Adding up col 0 (Left):
    col0 = troysArray[0][0] + troysArray[1][0] + troysArray[2][0];
    cout << "The sum of col 0 equals: " << col0 << endl;

    //Adding up col 1 (Middle):
    col1 = troysArray[0][1] + troysArray[1][1] + troysArray[2][1];
    cout << "The sum of col 1 equals: " << col1 << endl;

    //Adding up col 2 (Right):
    col2 = troysArray[0][2] + troysArray[1][2] + troysArray[2][2];
    cout << "The sum of col 2 equals: " << col2 << endl;

    cout << "\n";

    //Adding up diagonal1 (topLeft-bottomRight)(dia 1):
    dia1 = troysArray[0][0] + troysArray[1][1] + troysArray[2][2];
    cout << "The sum of dia 1 equals: " << dia1 << endl;

    //Adding up diagonal2(bottomLeft-topRight)(dia 2):
    dia2 = troysArray[2][0] + troysArray[1][1] + troysArray[0][2];
    cout << "The sum of dia 2 equals: " << dia2 << endl;

}
return 0;
}
