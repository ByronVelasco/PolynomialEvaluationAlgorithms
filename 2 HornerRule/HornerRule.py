# %% [markdown]
# ## Horner's Rule

# %%
def HornerRule(coeff, x):
  """
  Horner's rule for evaluating a polynomial at a given point.
  
  Parameters:
  coeff (list): Coefficients of the polynomial.
  x (float): The point at which to evaluate the polynomial.
  
  Returns:
  float: The value of the polynomial at x.
  """
  result = 0
  for i in range(len(coeff)-1, -1, -1):
    result = result * x + coeff[i]
  return result


