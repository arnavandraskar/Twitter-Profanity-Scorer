
# Twitter Profanity Scorer

The Twitter Profanity Scorer is a Python program that analyzes a given set of tweets and assigns them a profanity score based on the number of racial slurs they contain. The program reads in a CSV file of tweets, processes each tweet to determine its profanity score, and outputs the results to a new CSV file.

## Getting started

To use the Twitter Profanity Scorer, you'll need to have Python 3 and the pandas library installed. You can install pandas using pip:

```
pip install pandas

```

To run the program, download the code and save it as a Python file (e.g., profanity_scorer.py). Then, run the following command in your terminal:

```
python profanity_scorer.py

```
This will load the Twitter dataset, analyze each tweet, and output the results to a new CSV file.

### Usage
The program works by creating a `profanity` class, which loads a set of racial slurs from a file and provides a method for calculating the profanity score of a given tweet. The `__init__` method of the `profanity` class loads the set of racial slurs from the `racial_slurs`.txt file.

The `get_score` method of the `profanity` class takes a tweet as input and returns a profanity score ('clean', 'mild', 'moderate', or 'severe') based on the number of racial slurs in the tweet.

The main part of the program reads in a CSV file of tweets using the pandas `read_csv` function. It then creates an instance of the `profanity` class, and uses the `apply` function to apply the `get_score` method to each tweet in the dataset. The results are then saved to a new CSV file using the pandas `to_csv` function.








