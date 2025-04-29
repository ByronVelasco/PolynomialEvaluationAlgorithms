# **Experiment Engine: Polynomial Evaluation Machine**

This module provides the experimental engine used to evaluate and compare the time complexity of polynomial evaluation algorithms. It includes the visualization of the results.

## **Machine Overview**

- A set of grades of polynomials is defined in the variable `grades`.
- For each grade, the polynomial evaluation is repeated `reps` times to compute an **average execution time**. This reduces the impact of random system processes affecting timing.
- The algorithms to be tested are listed in `algorithm`.

The execution times are stored in a list called `total_times`, where each entry corresponds to the average time for a specific algorithm.

---

## **Complexity Machine**

  Validates the **theoretical time complexity** of a single algorithm. It also allows to compare the execution time of both evaluation algorithms.

---

## **Graphs and Visualization**

The plots generated in this project are **line plots**, each titled according to the algorithm used. All graphs are saved in the `img/` folder of the project, and also displayed within the notebook.

### **Plotting Functions**

- `ComplexityGraph`:

  Used to plot the results obtained for a single algorithm.

- `ComparisonGraph`:  

  Used to plot the results obtained for both algorithms.

---

## **MachineCall Utility**

The function `MachineCall` acts as a controller. Based on the input data, it decides whether to use `ComplexityGraph` or `ComparisonGraph`, ensuring that the appropriate logic and graphing function is triggered.

---

This experimental engine is designed for academic and educational use, to help visualize how sorting algorithms behave in practical conditions.