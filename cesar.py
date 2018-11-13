# імпорт модуля sys для читання аргументів командного рядка
import sys
# збережемо алфавіт мови для пошуку в ньому і підстановки нових літер
alphabet = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'
# читаємо текст, який слід закодувати; одразу змінюємо регістр
text = sys.argv[1].lower()
# читаємо зсув для кодування
shift = int(sys.argv[2])
# оголошуємо змінні для закодованого тексту, закодованої окремої літери, та номеру літери в алфавіті
coded_text = ''
new_letter = ''
letter_position = None
# пробігаємо весь початковий текст
for letter in text:
    # шукаємо поточний символ в алфавіті
    letter_position = alphabet.find(letter)
    # якщо він там присутній, вираховуємо позицію закодованої літери - зі зсувом - і вибираємо літеру алфавіту з новим номером
    if letter_position != -1:
        new_letter = alphabet[(letter_position + shift) % len(alphabet)]
        # інакше залишаємо символ без змін (пробіли, розділові знаки та ін.)
    else:
        new_letter = letter
        # додаємо символ до закодованого повідомлення
        coded_text = coded_text + new_letter
        # виводимо
        print(coded_text)