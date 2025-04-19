# %% [markdown]
# ## Naive Polynomial Evaluation

# %%
def NaiveEvaluation(coeff, x):
  """
  Naive evaluation of a polynomial at a given point x.
  :param coeff: list of coefficients
  :param x: point to evaluate the polynomial at
  :return: value of the polynomial at x
  """
  n = len(coeff)
  result = 0
  for i in range(n):
    result += coeff[i] * (x ** i)
  return result


