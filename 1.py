# 1. ফাংশন ব্যবহার  করে List এর পাঁচটি সংখ্যাকে যোগ করার Program লেখ।
'''
numbers_list = [1, 2, 3, 4, 5]
def sum_of_numbers(numbers):
    total = 0
    for number in numbers:
        total= total+ number
    return total

print(sum_of_numbers(numbers_list))

'''
# code explaination: 
# Step-1: List তৈরি হচ্ছে step-2: Function তৈরি হচ্ছে step-3: Function Call হচ্ছে step-4: total Variable তৈরি step-5: for loop শুরু:
#print(sum([1, 2, 3, 4, 5])) 
# 2. ফাংশন ব্যবহার  করে ধনাত্মক  পূর্ণ সংখ্যার Factorial এর মান নির্ণয় করার program লেখ। 
# ফাংশন ব্যবহার করে ধনাত্মক পূর্ণ সংখ্যার Factorial নির্ণয়
'''
def factorial(number):
    fact = 1

    for i in range(1, number + 1): #১ থেকে number পর্যন্ত সংখ্যা তৈরি করো
        fact = fact * i

    return fact


num = int(input("Take a positive integer: "))

if num < 0:
    print("Factorial is not positive number.")
else:
    result = factorial(num)
    print("Factorial =", result)
'''
#  3. ফাংশন ব্যবহার করে ত্রিভুজ ক্ষেত্রের ক্ষেত্রফল নির্ণয়ের প্রোগ্রাম লেখো।

def triangle_area(b, h):
    return 0.5 * b * h

print(triangle_area(10, 5))
