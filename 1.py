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
#print(sum([1, 2, 3, 4, 5])) 
# 2. ফাংশন ব্যবহার  করে ধনাত্মক  পূর্ণ সংখ্যার Factorial এর মান নির্ণয় করার program লেখ। 
    