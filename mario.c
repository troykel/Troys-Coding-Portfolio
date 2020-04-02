//Troy Kelley - CS50 - Week 1
#include <stdio.h>

int main(void) {
int maxrows;
int rows;
int colstars;
int colspaces;
int counter = 0;

do {
    printf("What is the number of rows in your pyramid?? ");
    scanf("%d", &maxrows);
    counter += 1;
/*Next line makes sure that input's been requested at least once (otherwise the error message is shown before the user      even responds to the first question!) It also checks that the input is in  range.*/
    if (counter >= 1 && ((maxrows < 1) || (maxrows > 8))) {
        printf("Your entry is out of range(1-8) \n");}
    }
while (!((maxrows >=1) && (maxrows <= 8)));

//The next line prints the rows of BOTH triangles.
for (rows = 1; rows <= maxrows; rows++) {
    for (colspaces = maxrows - rows; colspaces >= 0; colspaces--){
        printf(" ");
    }
    //The line below finishes the printing (the columns) of the //    //first triangle.
    for (colstars = 1; colstars < rows + 1; colstars++){
        printf("#");
    }
    //The next (printf) line is what creates the gap of 2 spaces 
    //between the first and second triangles.
    printf("  ");
    //The next line finishes the printing (the columns) of the
    //second triangle. 
    for (colstars = 1; colstars <= rows; colstars++) 
    {
        printf("#");
    }
    {
    //The next line is necessary, otherwise all the stars will be
    //printed on the same line.
    printf("\n");
  
   
}
}}
