# **Complexity of Polynomial Evaluation Algorithms**

## **Summary**

This project explores and compares different algorithms for polynomial evaluation, focusing on their computational complexity and practical performance. The core aim is to analyze how algorithmic design impacts execution time, especially when dealing with high-degree polynomials.

## **Objectives**

- To implement and test different methods of polynomial evaluation.
- To measure and compare their performance through computational experiments.
- To validate theoretical time complexity using empirical data.
- To build a modular and extensible codebase for future testing or algorithm inclusion.

## **Conclusions**

The Naive Evaluation method has a quadratic time complexity O($n^2$) as it computes each power of `x` explicitly. In contrast, the Horner’s Rule method has a linear time complexity O($n$), achieved by rewriting the polynomial in nested form to minimize operations. The experiments confirmed the theoretical behavior, showing that Horner's Rule is significantly faster for high-degree polynomials. Therefore, for practical and large-scale applications, Horner’s Rule is the preferred method due to its efficiency.

## **Project Structure**

The repository is organized into the following components:

- **`Naive and Horner`** Folder:  
  This folder contains the implementation of algorithms `naive_evaluation` and `horner_rule` and their performance comparison with each other. It includes an experiment measuring and analyzing their execution times.

- **`img` Folder**:  
  Stores the output images generated during experimentation.

- **`project_functions` Python Script**:  
  This Python script includes both algorithms developed specifically for this project.

- `requirements.txt` Text File:   
  This file lists all the dependencies required to run the project.

## **Final Note**

The system developed for this project was created solely for academic purposes. It is not designed to be an optimal or production-grade benchmarking tool.

## **Reference**

This project follows the structure and theoretical foundations presented in the following textbook:

> Cormen, Thomas H., Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein.  
> *Introduction to Algorithms*. Fourth Edition.  
> Cambridge, Massachusetts; London, England: The MIT Press, 2022.  
> ISBN: 9780262046305  
> LCCN: 2021037260  
> Available at: [https://lccn.loc.gov/2021037260](https://lccn.loc.gov/2021037260)

## **License**

- The **source code** of this project is licensed under the [MIT License](./LICENSE).  
  You are free to use, modify, and distribute the code with proper attribution.

- The **educational content** (including explanations, diagrams, and documentation) is shared under the  
  [Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/).  
  You may reuse and adapt it for non-commercial purposes with attribution.

---

© 2025 Byron Velasco