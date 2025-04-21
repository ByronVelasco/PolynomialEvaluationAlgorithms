# NaiveEvaluation

This module contains the file `NaiveEvaluation.ipynb`, which implements the naive polynomial evaluation.

## NaiveEvaluation Algorithm

The naive method for evaluating a polynomial consists of directly computing each term using the formula:

$P(x) = a_0 + a_1 x + a_2 x^2 + \dots + a_n x^n$

This approach uses explicit exponentiation for each term. While easy to implement, it is not efficient.

## Function: `NaiveEvaluation(coeff, x)`

Evaluates the polynomial with coefficients `coeff` at point `x`.

**Example:**
```python
coeff = [2, 6, 9, 5, 8]
x = 2
result = NaiveEvaluation(coeff, x)
print(result)
# Output: 218
```

## Time Complexity

- **Big-Oh:** $O(n^2)$

---

© 2025 Byron Velasco