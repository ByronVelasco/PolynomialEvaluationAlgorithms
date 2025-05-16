# **Naive Polynomial Evaluation**

Naive polynomial evaluation computes the value of a polynomial at a given point by directly substituting the value into the polynomial and calculating each term separately. For a polynomial of degree n, this approach requires evaluating each power of the variable and multiplying it by the corresponding coefficient, then summing all terms. This method is straightforward but can be inefficient for high-degree polynomials due to repeated calculations of powers.

For simplicity, we represent $P_n(x)=a_0+a_1x+a_2x^2+\dots+a_nx^n$

## **Function:** `naive_evaluation(coeff, x)`

Evaluates the polynomial with coefficients `coeff` at point `x`.

**Example:**
```python
coeff = [2, 6, 9, 5, 8]
x = 2
result = naive_evaluation(coeff, x)
print(result)
# Output: 218
```

## **Time Complexity**

- **Big-Oh:** $O(n^2)$

# **Horner's Rule**

Horner's Rule is an efficient algorithm for evaluating polynomials. Instead of computing each term's power separately, it rewrites the polynomial in a nested form to minimize the number of multiplications. For a polynomial $P_n(x) = a_0 + a_1x + a_2x^2 + \dots + a_nx^n$, Horner's Rule expresses it as $P_n(x) = a_0 + x(a_1 + x(a_2 + \dots + x(a_{n-1} + x a_n)))$. This approach reduces computational complexity and improves numerical stability.

## **Function:** `horner_rule(coeff, x)`

Evaluates the polynomial with coefficients `coeff` at point `x`.

**Example:**
```python
coeff = [2, 6, 9, 5, 8]
x = 2
result = horner_rule(coeff, x)
print(result)
# Output: 218
```

## **Time Complexity**

- **Big-Oh:** $O(n)$

---

© 2025 Byron Velasco