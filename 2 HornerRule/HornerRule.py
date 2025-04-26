# %% [markdown]
# ## Horner's Rule

# %%
def HornerRule(coeff, x):
  result = 0
  for i in range(len(coeff)-1, -1, -1):
    result = result * x + coeff[i]
  return result


