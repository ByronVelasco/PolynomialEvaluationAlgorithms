# %% [markdown]
# ## Naive Polynomial Evaluation

# %%
def NaiveEvaluation(coeff, x):
  n = len(coeff)
  result = 0
  for i in range(n):
    result += coeff[i] * (x ** i)
  return result


