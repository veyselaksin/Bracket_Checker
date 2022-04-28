# BRACKET CHECKER

Algoritmada Checker adlı bir sınıf vardır ve bu sınıf string bir değer alır. Checker sınıfı ayrıca isBalanced adlı bir fonksiyona sahiptir. Bu fonksiyon verilen string içerisinde yer alan parantezlerin doğru kullanılıp kullanılmadığını kontrol eder. Eğer doğru bir kullanım söz konusu ise EVET, değilse HAYIR değerini döndürür.


Algoritma oluşturulurken open_brackets, close_brackets adında iki adet dizi kullanılmıştır. 

```python
open_brackets = ["{", "[", "("]
close_brackets = ["}", "]", ")"]
```

Bu diziler parantezlerin açılış ve kapanış etiketlerini temsil etmektedir. Açılış ve kapanış etiketlerinin olduğu dizileri zip fonksiyonu kullanılarak her bir açılış elemanı kendi kapanış elemanı ile birleştirilir. Ardından sözlük yapısı kullanılarak anahtar, değer ilişkisi elde edilir. 

``` python
open_brackets = ["{", "[", "("]
close_brackets = ["}", "]", ")"]
brackets = dict(zip(open_brackets, close_brackets))
```

Her açılış etiketi stack adında bir diziye aktarılır. Kapanış etiketine denk gelindiği zaman stack içerisinde bulunan en üstteki açılış etiketinin değeri ile kapanış etiketinin değeri karışlaştırılır. Eğer değerler birbirine eşit değilse fonskiyon "NO" değerini döndürür. Ayrıca stack içerisi boş değilse de fonksiyon "NO" değerini döndürür. Eğer işlemler başarılı olursa fonksiyon varsayılan olarak "YES" değerini döndürür.

```python
class Checker:

    open_brackets = ["{", "[", "("]
    close_brackets = ["}", "]", ")"]
    brackets = dict(zip(open_brackets, close_brackets))
    stack = list()

    def __init__(self, string):
        self.string = string

    def isBalanced(self):
        
        for i in self.string:
            if i in self.open_brackets:
                self.stack.append(i)

            elif i in self.close_brackets:
                if not self.stack or i != self.brackets[self.stack.pop()]:
                    return "NO"
        
        return "YES"

```

## Kullanım
```sh
git clone https://github.com/veyselaksin/Bracket_Checker.git

cd
```
