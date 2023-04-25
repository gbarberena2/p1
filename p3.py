from scipy.stats import poisson

# Parámetros
lambda_param = 1500
k = 1480

# Calcular la probabilidad acumulativa (CDF) hasta k
cdf = poisson.cdf(k, lambda_param)

# Calcular el complemento (1 - CDF)
probabilidad = 1 - cdf

print(probabilidad)
