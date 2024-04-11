def mapper(line):
  """
  Map function: разбивает строку на слова и возвращает список пар (слово, 1)
  """
  for word in line.strip().split():
    yield word.lower(), 1

def reducer(word, counts):
  """
  Reduce function: суммирует количество вхождений каждого слова
  """
  yield word, sum(counts)

def mapreduce(text):
  """
  Основная функция MapReduce:
   1. Применяет map функцию к каждой строке текста.
   2. Группирует результаты по слову.
   3. Применяет reduce функцию к каждой группе.
  """
  # Имитация Map этапа
  mapped_data = []
  for line in text.splitlines():
    mapped_data.extend(mapper(line))

  # Имитация Shuffle этапа (группировка по ключу)
  grouped_data = {}
  for word, count in mapped_data:
    if word not in grouped_data:
      grouped_data[word] = []
    grouped_data[word].append(count)

  # Имитация Reduce этапа
  result = {}
  for word, counts in grouped_data.items():
    result[word] = next(reducer(word, counts))

  return result

# Пример использования
with open('90202836.txt') as f:
    text = f.readlines()
f.close()

my_string = " ".join(str(element) for element in text)

word_counts = mapreduce(my_string)

# Вывод результатов
for word, count in word_counts.items():
  print(f"{word}: {count}")