# Python Financial and Election Analysis

This repository contains Python scripts for analyzing financial and election data. The scripts, `PyBank.py` and `PyPoll.py`, are designed to read CSV files containing financial and election data, respectively, and produce analysis reports in text format.

## PyBank

The `PyBank.py` script analyzes financial data to calculate various metrics such as total months, total profit/losses, average changes, and the greatest increase and decrease in profits over a period.

### Usage

1. Ensure you have Python installed on your machine.
2. Navigate to the `PyBank` folder.
3. Place your financial data CSV file named `budget_data.csv` in the `PyBank` folder.
4. Run the script using the command `python PyBank.py`.
5. View the analysis report in the generated text file `budget_analysis.txt`.

### Example Output

Financial Analysis:
----------------------------------------------------------------------------
The total number of months included in the data set:  86

Total amount of profit/losses over the entire period:  22564198

The average changes in profit/losses over the entire period:  -8311.11

Greatest increase in profit:  1862002.0

Greatest decrease in profit:  -1825558.0

## PyPoll

The `PyPoll.py` script analyzes election data to calculate various metrics such as the total number of votes cast, list of candidates who received votes, the percentage of votes each candidate won, and the winning candidate.

### Usage

1. Ensure you have Python installed on your machine.
2. Navigate to the `PyPoll` folder.
3. Place your election data CSV file named `election_data.csv` in the `PyPoll` folder.
4. Run the script using the command `python PyPoll.py`.
5. View the analysis report in the generated text file `election_analysis.txt`.

### Example Output

Total number of votes cast:  369711

List of candidates who received votes:  
- Charles Casper Stockham
- Diana DeGette
- Raymon Anthony Doane

The percentage of vote each candidate won: 
| Candidate                 | Ballot ID | Percentage |
|---------------------------|-----------|------------|
| Charles Casper Stockham   | 85213     | 23.049     |
| Diana DeGette             | 272892    | 73.812     |
| Raymon Anthony Doane      | 11606     | 3.139      |

The candidate that has the highest vote by percentage: Diana DeGette

## References

- Data Structures. Python documentation. (n.d.). [https://docs.python.org/3/tutorial/datastructures.html](https://docs.python.org/3/tutorial/datastructures.html)
- GeeksforGeeks. (2023a, September 29). How to calculate the percentage of a column in pandas ?. [https://www.geeksforgeeks.org/how-to-calculate-the-percentage-of-a-column-in-pandas/](https://www.geeksforgeeks.org/how-to-calculate-the-percentage-of-a-column-in-pandas/)
- GeeksforGeeks. (2023b, September 29). How to calculate the percentage of a column in pandas ?. [https://www.geeksforgeeks.org/how-to-calculate-the-percentage-of-a-column-in-pandas/](https://www.geeksforgeeks.org/how-to-calculate-the-percentage-of-a-column-in-pandas/)
- Markov, Z., Riley, A., user1718097, Zero, cottontail, & emada. (1961, August 1). Find the column name which has the maximum value for each row. Stack Overflow. [https://stackoverflow.com/questions/29919306/find-the-column-name-which-has-the-maximum-value-for-each-row](https://stackoverflow.com/questions/29919306/find-the-column-name-which-has-the-maximum-value-for-each-row)
- Willems, K. (2021, May 17). Pandas cheat sheet for data science in Python. DataCamp. [https://www.datacamp.com/cheat-sheet/pandas-cheat-sheet-for-data-science-in-python](https://www.datacamp.com/cheat-sheet/pandas-cheat-sheet-for-data-science-in-python)
- YouTube. (2022, December 24). How to convert python output to TXT file! (easy). [https://www.youtube.com/watch?v=FNOpWah3saA](https://www.youtube.com/watch?v=FNOpWah3saA)

Other resourceful ideas were gotten from class activities and office hours.


