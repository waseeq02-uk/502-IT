---

## Project Overview

The assignment includes **three main parts**:

### 1. Delivery Route Optimisation (TSP)

* Solves a delivery routing problem using the **Nearest Neighbour** algorithm
* Improves the route using **2-opt local search**
* Demonstrates use of graph algorithms and heuristics

### 2. Dynamic Resource Allocation

* Implements a **priority-based CPU scheduler**
* Uses a **binary heap** for efficient scheduling
* Includes an **aging mechanism** to reduce starvation

### 3. Recommendation Engine

* Builds a simple **book recommendation system**
* Uses **user-user collaborative filtering**
* Applies **Jaccard similarity** and an **inverted index**

---

## Technologies Used

* Python
* Data structures (heaps, graphs)
* Greedy algorithms and local search
* Scheduling algorithms
* Basic recommendation systems
* Unit testing with pytest

---

## How to Run the Project

### Install dependencies

```
pip install -r requirements.txt
```

### Run the main demo

```
python main.py
```

This will:

* Run the TSP algorithm
* Run the scheduler simulation
* Show book recommendations for a sample user

---

## Running Tests (Optional)

Unit tests are included to check individual parts of the code.

Run tests using:

```
python -m pytest
```

---

## Notes

* The project is designed to run fully using `main.py`
* Tests are included for verification but are not required to run the program
* Code is organised using a `src/` folder structure

## Author

**[Waseeq Ahmed]**
Student ID: **[15146137]**
Module: Applied Algorithms and Data Structures (502IT)
