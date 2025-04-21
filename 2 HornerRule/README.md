# HornerRule

This module contains the file `HornerRule.ipynb`, which implements the Horner's rule for polynomial evaluation.

## HornerRule Algorithm

### Horner’s Rule

Horner’s rule is an efficient method for evaluating polynomials that reduces the number of multiplications required. Instead of computing each power of *x* separately, it rewrites the polynomial in nested form:

$P(x) = a_0 + x(a_1 + x(a_2 + ... + x(a_{n-1} + x\cdot a_n))$

This approach is efficient for large-degree polynomials.

## Function: `HornerRule(coeff, x)`

Evaluates the polynomial with coefficients `coeff` at point `x`.

**Example:**
```python
coeff = [2, 6, 9, 5, 8]
x = 2
result = HornerRule(coeff, x)
print(result)
# Output: 218
```

## Time Complexity

- **Big-Oh:** $O(n)$

---

© 2025 Byron Velasco