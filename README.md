# Shakespearean Sonnet Generator

![Shakespeare's Sonnets](link-to-an-image-if-any)

## Overview

This project is a Shakespearean Sonnet generator based on n-gram modeling. It utilizes NLTK for text processing and Streamlit for creating a user interface. The generated sonnets mimic the style of William Shakespeare.

## Getting Started

### Prerequisites

Make sure you have the required libraries installed. You can install them using:

```bash
pip install -r requirements.txt
```

### Usage

1. Clone the repository:

```bash
git clone https://github.com/arpy8/ArpitSengar_TaskRound_GDSC_VITB.git
cd ArpitSengar_TaskRound_GDSC_VITB
```

2. Run the Streamlit app:

```bash
streamlit run streamlit_app.py
```

3. Adjust the number of lines using the provided input and click "Submit" to generate sonnets.

## Code Structure

- `streamlit_app.py`: Main application script that uses NLTK and Streamlit to generate and display Shakespearean sonnets.
- `data/Sonnets.txt`: Text file containing Shakespeare's sonnets for training the n-gram model.
- `notebook/Shakespeare’s Sonnets.ipynb`: Jupyter Notebook that I used during the development stage.
- `assets/banner.png`: Contains the banner image for readme.

## Configuration

- `ngram_model`: The script uses an n-gram model to generate sonnets. You can experiment with different values of `n` for varied results.

## Example

```python
# Generate 5 sonnets with 10 lines each
create_sonnet(5)
```

## Contributors

- [arpy8](https://github.com/arpy8)

## Acknowledgments

- This project is inspired by the timeless works of William Shakespeare.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.