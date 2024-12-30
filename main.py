import pandas as pd
import matplotlib.pyplot as plt

comments=pd.DataFrame({
    'Comment': [
        'Amazing product! Absolutely love it.',
        'Not a good experience. Very disappointing.',
        'The service was okay, nothing special.',
        'I loved it! Will definitely recommend to my friends.',
        'Worst product ever! Waste of money.',
        'Very bad quality, will never buy again.',
        'Good quality and affordable. Happy with the purchase.',
        'Neutral feelings about it, neither good nor bad.',
        'Excellent quality and very affordable, highly recommend.',
        'The product broke after a week of use, very poor.',
        'Best purchase I have made this year!',
        'Mediocre product, could be better.',
        'The product exceeded my expectations. Very happy!',
        'Not bad, but could be improved.',
        'I don’t like it. Not worth the price.'
    ]
})

def analysis(comments):
  
  positive_response=['amazing','love','good','happy','impressed','satisfy','excellent','best']
  negative_response=['disappoint','worst','waste','bad','poor']
  comments=comments.lower()
  
  if any(content in comments for content in positive_response):
    return 'Positive'
  elif any(content in comments for content in negative_response):
    return 'Negative'
  else:
    return 'Neutral'

comments['Sentiments']=comments['Comment'].apply(analysis)    
sentiment_counts = comments['Sentiments'].value_counts()
plt.figure(figsize=(8,6))
plt.bar(sentiment_counts.index, sentiment_counts.values,color=['blue','green','red'])
plt.ylabel('Number of comments')
plt.ylim(0,10)
plt.xlabel('Response')
plt.title('\nProduct Review Analysis\n')
plt.show()

print('Public Sentiments:')
for index, row in comments.iterrows():
    print(f"Comment: {row['Comment']}\nSentiment: {row['Sentiments']}\n")
    

    
  
