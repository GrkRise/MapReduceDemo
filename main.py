def mapper(key, value):
  """
  Mapper function:
  - key: (i, k) - индексы строки и столбца элемента матрицы A
  - value: значение элемента
  - Выход: список пар (j, a_ik * b_kj) для каждого столбца j в матрице B
  """
  i, k = key
  result = []
  for j in range(len(matrix_B[0])):
    result.append((j, (i, value * matrix_B[k][j])))
  return result

def reducer(key, values):
  """
  Reducer function:
  - key: j - индекс столбца
  - values: список (i, a_ik * b_kj) для всех k
  - Выход: (i, j, сумма a_ik * b_kj для всех k)
  """
  sum = 0
  i = None
  for i_k, value in values:
    i = i_k
    sum += value
  return (i, key, sum)

# Пример матриц
matrix_A = [[1, 2, 3], [4, 5, 6]]
matrix_B = [[7, 8], [9, 10], [11, 12]]

# "Map" этап - имитация
mapped_data = []
for i in range(len(matrix_A)):
  for k in range(len(matrix_A[0])):
    mapped_data.extend(mapper((i, k), matrix_A[i][k]))

print(mapped_data)

# Группировка по ключу (имитация shuffle)
grouped_data = {}
for key, value in mapped_data:
  if key not in grouped_data:
    grouped_data[key] = []
  grouped_data[key].append(value)

print(grouped_data)

# "Reduce" этап - имитация
result_matrix = []
for key, values in grouped_data.items():
  result_matrix.append(reducer(key, values))

# Печать результата
print(result_matrix)