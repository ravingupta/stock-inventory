# Stock-Inventory
## Stock Tracker and ETF Analyzer

Welcome to the **Stock-Inventory**, an open-source Python Flask application designed for educational purposes! This project is a simple yet powerful tool to help users create and manage their personalized list of stocks and ETFs, track prices, and compare them with their purchase prices.

---

## Purpose
The primary goal of this project is **educational**. It serves as a hands-on learning experience, offering in-depth insights into various technologies while providing a practical example to understand requirements and their implementation effectively.

![Project Screenshot](./docs/project-demo(1).png)

---

## Technology Stack

### Framework
- **Flask**: Lightweight web framework for building scalable and simple applications.

### Libraries
- **BeautifulSoup**: Web scraping and crawling for fetching real-time stock and ETF data.
- **Pandas**: Data analysis and manipulation for managing user data and performing calculations.
- **pytest**: Comprehensive unit testing for ensuring code quality and reliability.

### Storage
- **In-Memory Database**: Custom database for faster operations.
- **CSV Backup**: Persistent storage for user data.

---

## Features

### Core Features
- **Custom Watchlist**: Add your stocks and ETFs to your personalized list for easy tracking.
- **Price Tracking**: Monitor current stock and ETF prices and compare them to your purchase price.
- **In-Memory Database**: Data handling using an in-memory storage to keep things simple, backed up in CSV for persistence.
- **Data Handling**: Utilize **Pandas** for seamless data manipulation and analysis.

### Planned Extensions
- **ETF Holdings Details**: Fetch and display details of ETF holdings.
- **Unified Stock Inventory View**: See how much of each stock you own across multiple ETFs, integrated into a single, comprehensive view.

---

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/ravingupta/stock-inventory.git
    cd stock-inventory
    ```

2. **Install dependencies**: Make sure you have Python 3.8+ installed.
    ```bash
    pip install -r requirements.txt
    ```
3. **Run the application**:
    ```bash
    flask --app app run
    ```
4. Access the application: Open http://127.0.0.1:5000 in your browser.

---

## Usage

### Add Stocks or ETFs
- Use the web interface to input stock/ETF symbols and purchase details.

### Compare Prices
- View your stocks/ETFs against the prices at which you purchased them.

### Backup Data
- The data is periodically backed up to a CSV file for recovery or external use.

---
## Testing
Run the test suite to ensure all functionalities work as expected:
    ```bash
    pytest
    ```

---

## Contributions
This project is open for contributions! Whether it's bug fixes, feature enhancements, or documentation updates, feel free to fork the repository and submit a pull request.

---

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

---

## Roadmap
- Fetch detailed holdings of ETFs.
- Provide a unified stock inventory view for ETF holdings and direct stock purchases.
- Add more robust error handling for web crawling and data updates.
- Explore integrating external APIs for improved stock/ETF data accuracy.
- Integrate free APIs / data source for realtime tracking of stock prices

---

## Acknowledgments
- **BeautifulSoup** for web crawling.
- **Pandas** for making data handling effortless.
- **pytest** for simplifying unit testing.

---

Happy tracking and analyzing your investments! 🚀