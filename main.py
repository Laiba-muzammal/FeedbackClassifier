import pandas as pd
from analyzer import analyze_sentiment
from plotter import plot_sentiment_distribution
from comments_data import comments

def main():
    df = pd.DataFrame({'Comment': comments})
    df['Sentiments'] = df['Comment'].apply(analyze_sentiment)

    sentiment_counts = df['Sentiments'].value_counts()
    plot_sentiment_distribution(sentiment_counts)

    print('Public Sentiments:\n')
    for _, row in df.iterrows():
        print(f"Comment: {row['Comment']}\nSentiment: {row['Sentiments']}\n")

if __name__ == "__main__":
    main()
