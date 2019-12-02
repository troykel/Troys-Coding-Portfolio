// Simple ToDo List C++.cpp : Defines the entry point for the console application.
// Courtesy of Jason Allison Roozenburg (See https://www.stackoverflow.com), who was so kind enough to have not only
// showed me the way to write a simple to-do list, but to also comment on how it's done as well!

//#include "stdafx.h"   edited out
#include <iostream>
#include <string>
#include <cstring>


using namespace std;



//function prototypes required in C++
int printvalues(string str1);



int main()
{
    string list_entry = "";

    std::cout << "What would you like to add to your to-do list?" << std::endl;

// while(true) is an infinite loop.  It exits when exit is sent to
// printvalues and it evaluates to the exit(0);  which means exit with an
// error code of 0.  Other way to exit a loop is with the break keyword.

    while (true) {
        getline(std::cin, list_entry);
        if (list_entry != "print") { printvalues(list_entry); }
        if (list_entry == "print") { printvalues("print"); }

    }
    // return required by most compilers is an int.  main is an int in this
    // program so return returns an int value.
    return 0;
};

// function "definition" for the function we put at the top.  defines the
// body of the function
int printvalues(string str1) {
    // static variables in C++ will retain their set values next time this
    // function is called within printvalues(list_entry) or
    // printvalues("print") or printvalues("exit")
    static int i = 0;
    static string all[30];

    // if list_entry is not the word print, (!= print) add the value at index i and
    // increment i using i++;
    if (str1 != "print") { all[i] = str1; i++; }

    //iterator i2
    int i2;

    // if we typed print inside the while (true) loop in main then print all
    // the values in a for loop starting at all[i2].
    if (str1 == "print") {
        for (i2 = 0; i2 < i; i2++) {
            //print i2 + 1 makes the value start at 1 so we don't print out
            // 0) Make the bed , we print out 1)
            cout << i2 + 1 << ")" << all[i2] << endl;
        }
    }
    // if exit was typed then the values are stored but it doesn't matter
    // because they aren't printed and the program exits with an error code
    // of 0, which is success.
        if (str1 == "exit") { exit(0); }
    return 0;
}
