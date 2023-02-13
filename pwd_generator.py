import random
import string
import secrets
import strgen

for i in range(1):
    # get random string of length 6 without repeating letters
    result_str = ''.join(random.sample(string.ascii_letters, 10))
  
    print("Print result: " + result_str)

secret_p = ''.join((secrets.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(10)))
print("Print Strong: " + secret_p )

random_str = strgen.StringGenerator("[\w\d]{8}").render()
print("Print Random Str" + random_str)

# random_str2 = strgen.StringGenerator("[\d]{3}&[\w]{3}&[\p]{2}").render()
# print("Another strong:"+ random_str2)
