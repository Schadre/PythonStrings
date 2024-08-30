""" 
Task 1: Keyword Highlighter

Write a program that searches through reviews list 
and looks for keywords such as "good", "excellent", "bad", "poor", and "average". 
We want you to capitalize those keywords then print out each review. 
Print out each review with the keywords in uppercase so they stand out.
""" 

reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]
# So for the first string in the reviews list, 
# we want it to say: 
# "This product is really GOOD. I'm impressed with its quality."

def keyword_highlighter():
    for i in range(len(reviews)):
        review = reviews[i]
        if "good" in review:
            review = review.replace("good", "GOOD")
        elif "excellent" in review:
            review = review.replace("excellent", "EXCELLENT")
        elif "bad" in review:
            review = review.replace("bad", "BAD")
        elif "Poor" in review:
            review = review.replace("Poor", "POOR")
        elif "average" in review:
            review = review.replace("average", "AVERAGE")
        reviews[i] = review
    print(reviews)

keyword_highlighter()



""" 
Task 2: Sentiment Tally

Develop a function that tallies the number of positive 
and negative words in each review.  The function should 
return the total count of positive and negative words.
""" 

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]


def review_counter():
    positive_count = 0
    negative_count = 0
    
    for review in reviews:
        review = review.lower()

        for word in positive_words:
            if word in review:
                positive_count += 1

        for word in negative_words:
            if word in review:
                negative_count += 1
    total_count = positive_count + negative_count
    return total_count
print(review_counter())
