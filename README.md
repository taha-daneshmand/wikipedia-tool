# Wikipedia Tool for Python

[![PyPI version](https://img.shields.io/pypi/v/wikipedia_tool.svg)](https://pypi.org/project/wikipedia_tool)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Downloads](https://img.shields.io/pypi/dm/wikipedia_tool.svg)](https://pypi.org/project/wikipedia_tool)

> **"Empowering your projects with the vast knowledge of Wikipedia!"**

---

## Overview

**Wikipedia Tool for Python** is a robust API wrapper that simplifies accessing and interacting with the [Wikipedia API](https://www.mediawiki.org/wiki/API:Main_page). With over 300 functions available (and more exciting features on the way!), this library lets you seamlessly search pages, extract summaries, retrieve full content, and much more—all with just a few lines of code.

Whether you're building a research tool, a chatbot, or just curious about Wikipedia data, **Wikipedia Tool** provides the power and flexibility to integrate Wikipedia into your Python projects.

---

## Key Features

- 🔍 **Search Pages:** Quickly search for relevant articles using keywords.
- 📄 **Retrieve Summaries & Content:** Easily extract summaries, full content, and additional metadata.
- 🔗 **Access Related Data:** Fetch images, links, categories, and references associated with a page.
- ⚙️ **Extensible & Future-Proof:** Over 300 functions available today—with plans for even more powerful features in upcoming releases.
- 🚀 **Easy to Use:** Simple installation and straightforward API designed for developers of all levels.

---

## Installation

Install the library using [pip](https://pip.pypa.io/en/stable/):

```bash
pip install wikipedia-tool
```

---

## Quick Start

Get started in just a few minutes:

```python
import wikipedia_tool as wp

# Search for a page related to Python programming
results = wp.search_page("Python programming")
print("Search Results:", results)

# Get a concise summary of the Python programming page
summary = wp.get_summary("Python programming")
print("Summary:", summary)

# Retrieve the full content of the page
content = wp.get_page_content("Python programming")
print("Content:", content)

# Explore many more functions to harness the power of Wikipedia data!
```

---

## Documentation

Comprehensive documentation is available in our [Wiki](https://github.com/taha-daneshmand/wikipedia-tool/wiki) and includes:

- Detailed API reference for all functions
- Code examples and tutorials
- Guidelines for contributing and adding new features

---

## Roadmap & Future Features

We are continuously working to make **Wikipedia Tool** even more powerful! Upcoming features include:

- **Enhanced Data Parsing:** More refined extraction for images, infoboxes, and tables.
- **Advanced Query Options:** Improved support for multi-language and cross-referenced data.
- **Customizable API Calls:** Tailor requests and responses to better suit your project needs.
- **Community-Driven Enhancements:** New functions and optimizations inspired by our user community.

Feel free to check our [Issues](https://github.com/taha-daneshmand/wikipedia-tool/issues) page to see what's coming up, or open a new issue if you have an idea or encounter any bugs!

---

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. If you'd like to contribute:

1. **Fork the Project**
2. **Create a Feature Branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit Your Changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the Branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

For detailed guidelines, please refer to our [CONTRIBUTING.md](CONTRIBUTING.md).

---

## License

This project is licensed under the [MIT License](LICENSE) © Taha Daneshmand.

---

## Stay Connected

- Follow us on [GitHub](https://github.com/taha-daneshmand/wikipedia-tool)
- Join the discussion on [Issues](https://github.com/taha-daneshmand/wikipedia-tool/issues)
- Spread the word and star the repo if you find it useful! ⭐

---

*Happy Coding!*
