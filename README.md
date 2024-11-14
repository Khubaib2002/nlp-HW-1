# NLP Assignments - Date Format Resolution, Wordpiece Algorithm, and Urdu Text Tokenization

This repository contains solutions for three NLP assignments: resolving ambiguities in date formats, implementing a simplified Wordpiece algorithm, and tokenizing Urdu text.

---

## Q1: Resolving Ambiguities Between DD/MM/YYYY and MM/DD/YYYY Date Formats

### Objective
To practice resolving ambiguities between two similar date formats (DD/MM/YYYY and MM/DD/YYYY) using contextual clues or logical assumptions.

### Approach
1. **Date Extraction**: Use regular expressions to extract dates in the DD/MM/YYYY or MM/DD/YYYY format from the input file.
2. **Format Resolution**: For each date, attempt to identify the format based on:
   - Contextual clues.
   - Logical assumptions, such as ruling out 13+ for months.
3. **Output**: Write identified dates and their interpreted formats to an output file, following naming conventions.

---

## Q2: Wordpiece Algorithm - First 10 Merges

### Objective
To simulate the initial steps of a Wordpiece algorithm by identifying the first 10 pairs of characters or subwords to be merged based on frequency scores.

### Approach
1. **Token Initialization**: Start with individual characters as tokens.
2. **Pair Merging**: Merge character pairs based on the formula:
   
   score = freq_of_pair / (freq_of_first_element * freq_of_second_element)

3. **Iteration**: Continue until 10 pairs are merged.

## Q3: Tokenizing Urdu Text

### Objective
To practice reading and tokenizing Urdu text, writing each token to an output file.

### Approach
1. **Read Urdu Text**: Read `urdu_text_input.txt` file.
2. **Tokenize**: Use libraries like `nltk`, `re`, or `UrduHack` to split the text into tokens.
3. **Output**: Write each token to an output file, one token per line.
