# Import the necessary libraries
import re
import pandas as pd

# Define a class to score the profanity level of a tweet
class profanity:
    def __init__(self):
        """
        Initializes the profanity class with a set of racial slurs from a file
        """
        # Load the set of racial slurs from a file called "racial_slurs.txt"
        with open('racial_slurs.txt', 'r') as f:
            # Read each line in the file and strip it of any whitespace
            # then store the resulting set of words as an attribute of the class
            self.racial_slurs = set([line.strip() for line in f])
         
    def get_score(self, line):
        """
        Takes a tweet and returns the degree of profanity based on the number of racial slurs contained in it
        
        Parameters:
        line (str): a string representing a tweet
        
        Returns:
        score (str): a string representing the degree of profanity based on the number of racial slurs
        """
        # Tokenize the sentence into individual words using a regular expression that matches any word
        words = re.findall(r'\b\w+\b', line)
        
        # Count the number of racial slurs in the tweet by checking each word against the set of racial slurs
        num_slurs = len([word for word in words if word.lower() in self.racial_slurs])
        
        # Assign a score to the tweet based on the number of racial slurs it contains
        if num_slurs == 0:
            score = 'clean'
        elif num_slurs == 1:
            score = 'mild'
        elif num_slurs <= 3:
            score = 'moderate'
        else:
            score = 'severe'
                
        return score
 
if __name__=='__main__':
    # Load twitter dataset from a csv file named "twitter.csv"
    df = pd.read_csv("twitter.csv")
    
    # Instantiate a profanity object to score the tweets
    score = profanity()
    
    # Apply the get_score method of the profanity object to each tweet in the dataset using a lambda function,
    # then store the results in a new column called 'degree_of_profanity'
    df['degree_of_profanity'] = df['tweet'].apply(lambda x: score.get_score(x))
    
    # Save the modified dataset to a new csv file called "twitter_scores.csv"
    df.to_csv('twitter_scores.csv', index= False)
