"""
https://leetcode.com/problems/design-spreadsheet/description/

A spreadsheet is a grid with 26 columns (labeled from 'A' to 'Z') and a given number of rows.
Each cell in the spreadsheet can hold an integer value between 0 and 105.

Implement the Spreadsheet class:

Spreadsheet(int rows) Initializes a spreadsheet with 26 columns (labeled 'A' to 'Z')
and the specified number of rows. All cells are initially set to 0.
void setCell(String cell, int value) Sets the value of the specified cell.
The cell reference is provided in the format "AX" (e.g., "A1", "B10"),
where the letter represents the column (from 'A' to 'Z') and the number represents a 1-indexed row.

void resetCell(String cell) Resets the specified cell to 0.
int getValue(String formula) Evaluates a formula of the form "=X+Y",
where X and Y are either cell references or non-negative integers,
and returns the computed sum.
Note: If getValue references a cell that has not been explicitly set using setCell,
its value is considered 0.

https://www.glassdoor.com/Interview/Implement-a-spreadsheet-where-one-can-update-a-cell-s-value-and-also-updates-other-cells-that-depend-on-it-similar-to-how-QTN_6526904.htm

https://www.1point3acres.com/bbs/thread-1111716-1-1.html
Coding was excel sheets. You have to implement two functions getCell() and setCell().
Handle cycles in sheet.
You're expected to write tests.
First part is okay to be implemented with sub-optimal getCell() implementation
where the value is computed on the fly.
Second part, the setCell() is supposed to update the values of impacted cells so that getCell() is O(1).
"""
# class Spreadsheet:

#     def __init__(self, rows: int):


#     def setCell(self, cell: str, value: int) -> None:


#     def resetCell(self, cell: str) -> None:


#     def getValue(self, formula: str) -> int:


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
