# Task 3 

[1](#1),
[2](#2),
[3](#3),
[4](#4),
[5](#5),
[6](#6),
[7](#7),
[8](#8),
[9](#9),
[10](#10),
[11](#11),
[12](#12),
[13](#13),
[14](#14),
[15](#15),
[16](#16),

## 1
```python
[i for i in range(1, 1001) if  i % 7 == 0 ]
```
## 2
```python
[i for i in range(1, 1001) if '2' in str(i)]
```
## 3
```python
a=[]
for i in range(1, 10001):
  if str(i) == str(i)[::-1]:
    a.append(i)
```
## 4
```python
string.count(' ')
```
## 5
```python
def delete_aeiou(text):
        return ''.join([letter for letter in text if letter not in 'aeiouAEIOU'])
```
## 6
```python
def delete_word(string):
   return  [word for word in string.split() if len(word) < 5]

```
## 7
```python
def get_dict(string):
    return  {word: len(word) for word in string.split()}
```
## 8
```python
result = {i for i in string  if i != ' ' and i != ':'}
```
## 9
```python
squared = map(lambda num: num ** 2, numbers)
```
## 10
```python
distance = {dot: (dot[0] ** 2 + dot[1] ** 2) ** (1/2) for dot in dots if dot[1] == 5 * dot[0] - 2}
```
## 11
```python
[i ** 2 for i in range(2, 28, 2)]
```
## 12
```python
result = max([(dot[0] ** 2 + dot[1] ** 2) ** (1/2) for dot in dots if dot[0] > 0 and dot[1] > 0])
```
## 13
```python
result = [(elem1 + elem2, elem1 - elem2) for elem1, elem2 in zip(num1, num2)]
```
## 14
```python
[str(int(elem) ** 2) for elem in stre if (int(elem) ** 2) % 2 == 0]
```
## 15
```python
def import_to_csv(input_str):
  import_tolist=[i.split(",") for i in input_str.split()]
  result =[i for i in zip(*import_tolist)]
  return result

```
## 16
```python
list(map(sum,zip(*a)))
```
    
