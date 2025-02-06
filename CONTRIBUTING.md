# Contributing to Wikipedia Tool for Python

First of all, thank you for your interest in contributing to **Wikipedia Tool for Python**! We welcome contributions from everyone—whether it's reporting bugs, suggesting new features, improving documentation, or writing code. Your help makes this project better for everyone.

---

## Table of Contents

- [How to Contribute](#how-to-contribute)
- [Getting Started](#getting-started)
- [Code Style Guidelines](#code-style-guidelines)
- [Pull Request Process](#pull-request-process)
- [Reporting Issues](#reporting-issues)
- [Community & Communication](#community--communication)
- [Code of Conduct](#code-of-conduct)

---

## How to Contribute

There are several ways you can help improve the project:

- **Report Bugs:** If you encounter a bug, please [open an issue](https://github.com/taha-daneshmand/wikipedia-tool/issues) with a clear description and steps to reproduce it.
- **Suggest Features:** Have an idea for a new feature or an improvement? Let us know by opening an issue so we can discuss it before you start working on it.
- **Improve Documentation:** Better documentation helps everyone! If you find something unclear or outdated in our docs, please submit a pull request with improvements.
- **Submit Code:** Whether you’re fixing a bug or adding a new feature, we welcome your pull requests. Please make sure your contributions follow our guidelines.

---

## Getting Started

To start contributing, follow these simple steps:

1. **Fork the Repository:**  
   Click the **Fork** button at the top right of the repository page to create your own copy.

2. **Clone Your Fork Locally:**

   ```bash
   git clone https://github.com/taha-daneshmand/wikipedia-tool.git
   cd wikipedia-tool
   ```

3. **Create a New Branch:**  
   Use a descriptive branch name that reflects your changes or the feature you're adding.

   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Install Dependencies:**  
   Ensure you have the necessary dependencies installed. It’s recommended to use a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

5. **Make Your Changes:**  
   Follow the [Code Style Guidelines](#code-style-guidelines) below to ensure consistency.

6. **Commit Your Changes:**  
   Write clear, descriptive commit messages. For example:

   ```bash
   git commit -m "Add new function to fetch page images"
   ```

7. **Push Your Changes and Open a Pull Request:**

   ```bash
   git push origin feature/your-feature-name
   ```

   Then, navigate to your fork on GitHub and open a pull request against the `main` branch.

---

## Code Style Guidelines

- **Follow PEP 8:**  
  Write clean, readable Python code that adheres to [PEP 8](https://www.python.org/dev/peps/pep-0008/).

- **Write Tests:**  
  If you add new functionality or fix bugs, please include tests to cover your changes. This helps maintain code quality and prevents future regressions.

- **Documentation:**  
  Update or add documentation when you make changes that affect the API or its usage.

- **Commit Messages:**  
  Use clear, descriptive commit messages that explain the “what” and “why” of your changes.

---

## Pull Request Process

1. **Sync with the Latest Changes:**  
   Before you submit a pull request, ensure your branch is up to date with the latest changes from the `main` branch.

2. **Describe Your Changes:**  
   In your pull request, explain what changes you have made and why. If the PR fixes an issue, mention it (e.g., “Fixes #123”).

3. **Ensure All Tests Pass:**  
   Your changes should not break any existing tests. Run the test suite locally before submitting your PR.

4. **Be Open to Feedback:**  
   Your pull request might receive comments or requests for changes. Please respond promptly and work collaboratively.

---

## Reporting Issues

If you encounter a bug or have an idea for improvement:

1. **Search Existing Issues:**  
   Check if someone has already reported the issue or suggested the feature.

2. **Open a New Issue:**  
   Provide a clear and descriptive title, and include the following:
   - A description of the issue or feature request.
   - Steps to reproduce the bug (if applicable).
   - Screenshots or error logs if available.
   - Your environment details (Python version, OS, etc.).

---

## Community & Communication

- **GitHub Issues & Discussions:**  
  Use [GitHub Issues](https://github.com/taha-daneshmand/wikipedia-tool/issues) to report bugs and discuss features.

- **Pull Requests:**  
  All code contributions should be made via pull requests. We appreciate your collaboration and will work with you to merge your changes as quickly as possible.

- **Stay Updated:**  
  Follow the repository to receive notifications about new issues, features, and discussions.

---

## Code of Conduct

This project adheres to a [Code of Conduct](CODE_OF_CONDUCT.md). By contributing, you agree to abide by its terms. Please report any unacceptable behavior to [tahadaneshmand.2009@proton.me].

---

Thank you for your contributions and for helping make **Wikipedia Tool for Python** even better!  
*Happy coding!*
