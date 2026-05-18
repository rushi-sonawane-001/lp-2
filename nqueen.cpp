#include <iostream>
using namespace std;

int board[10], n;

// Function to check safe position
bool safe(int row, int col)
{
    for(int i = 0; i < row; i++)
    {
        // Same column or diagonal
        if(board[i] == col || abs(board[i] - col) == abs(i - row))
            return false;
    }
    return true;
}

// Backtracking Function
bool solve(int row)
{
    // All queens placed
    if(row == n)
        return true;

    for(int col = 0; col < n; col++)
    {
        if(safe(row, col))
        {
            board[row] = col;

            // Recursive call
            if(solve(row + 1))
                return true;
        }
    }
    return false;
}

int main()
{
    cout << "Enter number of Queens: ";
    cin >> n;

    if(solve(0))
    {
        cout << "Solution:\n";

        for(int i = 0; i < n; i++)
        {
            for(int j = 0; j < n; j++)
            {
                if(board[i] == j)
                    cout << "Q ";
                else
                    cout << ". ";
            }
            cout << endl;
        }
    }
    else
    {
        cout << "No Solution";
    }
}