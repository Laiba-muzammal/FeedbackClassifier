def analyze_sentiment(comment):
    positive_keywords = ['amazing', 'love', 'good', 'happy', 'impressed', 'satisfy', 'excellent', 'best']
    negative_keywords = ['disappoint', 'worst', 'waste', 'bad', 'poor']

    comment = comment.lower()
    
    if any(word in comment for word in positive_keywords):
        return 'Positive'
    elif any(word in comment for word in negative_keywords):
        return 'Negative'
    else:
        return 'Neutral'
