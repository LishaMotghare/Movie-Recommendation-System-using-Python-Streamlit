# Movie Recommendation System

This project implements a simple movie recommendation system using content-based filtering. The system recommends movies based on the similarity of their cast and crew (director).

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [Files](#files)

## Introduction
This recommendation system analyzes movie data, extracts key features like cast and director, and then uses cosine similarity to find movies that are similar to a given input movie. The recommendations are served through a Streamlit web application.

## Features
- Recommends 5 similar movies based on an input movie title.
- Interactive web interface built with Streamlit.
- Data preprocessing for cast and director information.

## Setup
To set up and run this project locally, follow these steps:

1.  **Clone the repository (if applicable) or ensure you have the project files.**
2.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    The `requirements.txt` file contains:
    ```
    pandas
    scikit-learn
    streamlit
    ```

3.  **Ensure you have the data files:**
    - `Movie data.csv`: Contains the raw movie data.
    - `movie_list.pkl`: Pickled DataFrame of preprocessed movies.
    - `similarity.pkl`: Pickled similarity matrix used for recommendations.

## Usage
To run the Streamlit application, execute the following command in your terminal from the project's root directory:

```bash
streamlit run app.py
```

This will open a new tab in your web browser with the Streamlit application, where you can select a movie from a dropdown list and get recommendations.

## Files
- `Movie data.csv`: Original dataset containing movie information.
- `movie_list.pkl`: Preprocessed movie data saved as a Python pickle file.
- `similarity.pkl`: Cosine similarity matrix saved as a Python pickle file.
- `app.py`: The Streamlit application code.
- `requirements.txt`: List of Python dependencies for the project.
- `README.md`: This file, providing project documentation.
