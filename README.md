# Watch Next

This small application watch-next uses NLP to recommend movied based on the movie watched before.

## Table of Contents
- [Running the project](#installation)
- [Using Docker](#using-docker)

## Installation
To run watch-next follow these steps:

1. Clone the repository:

   [Repo](https://github.com/kudzaizvov/nlp-movie-recommendation.git)

2.  Navigate to the project directory:
3. Install the dependencies:
   * Create a Virtual env
      * python3 -m venv env   
      * source env/bin/activate
   * run `pip install -r /path/to/requirements.txt`
    
4. run `python watch_next.py`
  

## Using Docker
You can build a docker image using the following commands

1. `docker build -t <docker-tag> .`
2. `docker run <docker-tag>`
