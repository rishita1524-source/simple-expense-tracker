Simple Expense Tracker

# Overview

Simple Expense Tracker is a desktop application that allows you to easily record, categorize, and monitor your daily expenses. With a user-friendly interface and powerful features, it helps you maintain better control over your financial habits.

# Features

- Add Expenses: Record expenses with amount, category, description, and date
- View History: Browse through all your past expenses in an organized table
- Category Filtering: Filter expenses by categories for better analysis
- Data Persistence: Automatically saves your data locally
- Simple Interface: Clean and intuitive GUI built with Tkinter
- Cross-Platform: Works on Windows, macOS, and Linux

# Installation

# Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

# Usage

1. Adding an Expense:
   - Enter the amount in the "Amount" field
   - Select a category from the dropdown
   - Add an optional description
   - Choose the date (defaults to current date)
   - Click "Add Expense"

2. Viewing Expenses:
   - All expenses are displayed in the table below
   - Use the category filter to view specific categories
   - Click "Show All" to reset filters

3. Data Management:
   - Data is automatically saved to `expenses.json`
   - The file is created in the same directory as the application

#Project Structure

```
simple-expense-tracker/
├── expense_tracker.py    # Main application file
├── expenses.json         # Data storage file (auto-generated)
├── requirements.txt      # Python dependencies
└── README.md            # Project documentation
```

# Categories

The application comes with predefined expense categories:
- Food
- Transportation
- Shopping
- Utilities
- Healthcare
- Entertainment
- Education
- Other

# Technical Details

- Framework: Tkinter for GUI
- Data Storage: JSON file format
- Dependencies: 
  - `tkinter` (built-in Python library)
  - No external dependencies required

# Contributing

We welcome contributions! Please feel free to submit pull requests, report bugs, or suggest new features.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

# License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

# Author

Anamika Kumari
- GitHub: [@rishita1524-source](https://github.com/rishita1524-source)

# Acknowledgments

- Built with Python and Tkinter
- Inspired by the need for simple personal finance management tools

# Support

If you have any questions or run into issues, please open an issue on the GitHub repository.


Star this repo if you find it helpful!
