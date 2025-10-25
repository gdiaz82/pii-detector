# PII Detector

A multi-approach PII (Personally Identifiable Information) detection system combining Regex, Machine Learning, and LLMs for identifying sensitive data in text.

## Features

- **Regex Detection**: Pattern matching for emails, phones, credit cards, RUT
- **Multi-method Approach**: Regex (current), ML & LLMs (planned)
- **Context Awareness**: Keyword-based pattern detection
- **Structured Output**: JSON results with positions and confidence scores

## Installation

```bash
git clone https://github.com/gdiaz82/pii-detector.git
cd pii-detector
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows
pip install -r requirements.txt
