# Financial News & Stock Price Integration (Week 1)

**Predicting Price Moves with News Sentiment**

This repository contains the solution for the Week 1 Challenge at Nova Financial Solutions. The project focuses on Data Engineering, Financial Analytics, and Machine Learning Engineering to discover correlations between news sentiment and stock market movements.

## 📂 Project Structure

The project follows a modular Python structure to ensure reproducibility and scalability:

├── .github/ # CI/CD workflows
├── data/ # Raw and processed data
├── notebooks/ # Jupyter notebooks for exploration
├── src/ # Source code for data processing and analysis
│ ├── init.py
│ ├── loader.py # Data loading logic (DataLoader class)
│ └── analysis.py # Analysis logic (NewsAnalyzer, StockAnalyzer classes)
├── tests/ # Unit tests
├── requirements.txt # Python dependencies
└── README.md # Project documentation


## 🚀 Key Features

### 1. Exploratory Data Analysis (EDA)
- **Headline Analysis:** Statistical breakdown of headline lengths.
- **Publisher Insights:** Identification of top publishers and contribution frequency.
- **Time Series Trends:** Analysis of publication frequency over time to identify market-moving events.

### 2. Quantitative Analysis
- **Technical Indicators:** Implementation of financial indicators using `TA-Lib` and `pandas`.
    - **SMA (Simple Moving Average):** 20-day window.
    - **RSI (Relative Strength Index):** 14-day window to detect overbought/oversold conditions.
- **Visualization:** Automated generation of stock price vs. indicator plots.

## 🛠 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Isaacalex5371/challenge-week1
   cd challenge-week1

   1.Set up the virtual environment:
   python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

2.Install dependencies:
pip install -r requirements.txt

📊 How to Run
The analysis is modularized. You can run the analysis workflow directly from the notebooks or scripts.
Example Usage (Python):
from src.loader import DataLoader
from src.analysis import NewsAnalyzer, StockAnalyzer

# 1. Load Data
loader = DataLoader('../data/raw')
news_df = loader.load_news_data('raw_analyst_ratings.csv')

# 2. Analyze News
news_analyzer = NewsAnalyzer(news_df)
print(news_analyzer.get_headline_stats())
news_analyzer.plot_top_publishers()

# 3. Analyze Stocks
aapl_df = loader.load_stock_data('AAPL')
stock_analyzer = StockAnalyzer(aapl_df)
stock_analyzer.add_moving_average(window=20)
stock_analyzer.add_rsi(window=14)

📈 Visualizations
The project automatically generates insights such as:
.top_publishers.png: Bar chart of most active news sources.
.publication_trend.png: Time-series view of news volume.
.aapl_sma.png: AAPL price overlay with 20-day SMA.
.aapl_rsi.png: RSI momentum indicator.
🧪 Testing
Run the unit tests to ensure system stability:

pytest tests/

👤 Author
yishak alemayehu 
Week 1 - 10 Academy Challenge
code
Code
### Why this is better:
*   **It highlights `src`**: The tutors love seeing that you didn't just dump everything in a notebook.
*   **It explains the "How to Run"**: It shows the exact code snippet you are using, which proves you understand your own code.
*   **It lists the images**: Since your code saves `.png` files, the README mentions them as "Deliverables".

