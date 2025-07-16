import matplotlib.pyplot as plt

def plot_sentiment_distribution(sentiment_counts):
    plt.figure(figsize=(8, 6))
    plt.bar(sentiment_counts.index, sentiment_counts.values, color=['blue', 'green', 'red'])
    plt.ylabel('Number of Comments')
    plt.ylim(0, 10)
    plt.xlabel('Response')
    plt.title('\nProduct Review Analysis\n')
    plt.show()
