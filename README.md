# 🧠 FeedbackClassifier
A simple Python project to analyze user feedback and classify it into Positive, Negative, or Neutral sentiments based on keyword matching.

---

# 📌 Features
Classifies user comments using a basic keyword-based logic

Visualizes sentiment distribution using matplotlib

Clean and readable code suitable for learning or small-scale feedback systems

---

# 🗂️ Project Structure
```
FeedbackClassifier/
├── classifier.py       # Contains sentiment classification logic
├── visualizer.py       # Handles bar chart visualization
├── app.py              # Main script that integrates everything
└── README.md           # Project documentation
```

---

# 🚀 How It Works
The program takes a list of user comments.

Each comment is analyzed for presence of positive or negative keywords.

A sentiment tag is assigned to each comment.

A bar chart is generated showing the sentiment distribution.

---

# 📈 Sample Output
Positive keywords: "amazing", "love", "good", "happy", "excellent", "best", ..."

Negative keywords: "bad", "worst", "poor", "waste", "disappoint", ..."

> The tool prints each comment with its sentiment and plots the sentiment counts.

---

# ▶️ Run the App
#### Make sure you have matplotlib and pandas installed:

```
pip install matplotlib pandas
```

#### Run the project:
```
python app.py
```
