# FRAMEWORK_DECISION — Aryan Kandula

## Flask vs Streamlit

### Flask
- Lightweight Python web framework for custom applications.
- Requires routes, templates, and logic integration manually.
- Offers full control over structure and styling.
- Great for integrating existing console programs like Datamon.

### Streamlit
- Easier setup, auto-generates UI from Python scripts.
- Less customizable visually.
- Better for data dashboards, not detailed web apps.

## My Choice: Flask
**Reason:** I already have a Datamon checker function written in Python. Flask lets me reuse it easily and provides flexibility for a clean web page.

## Anticipated Challenge
Flask requires more manual setup (HTML templates and error handling), which might cause small bugs, but it gives me real control and learning.