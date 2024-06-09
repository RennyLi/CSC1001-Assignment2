
def is_anagram(s1,s2):  # define a function to check whether two words are anagram
    first_list=list(s1)
    second_list=list(s2)  # split the two words into two list
    list_one_sort=sorted(first_list)
    list_two_sort=sorted(second_list)  # sort the two lists
    if list_one_sort == list_two_sort:
        print("The two words are anagrams!")  # return true if the two sorted lists are identical
    elif list_one_sort != list_two_sort:
        print("The two words are not anagrams!")

def main():
    while True:
        s1=input("Please enter the first word:")  # prompt up the user to enter two words
        s2=input("Please enter the second word:")  # assign the two words to two variables s1, s2
        if s1 == s2:  # Consider the situation where the user will input two same words
            print("Please input two different words!")
        else:
            is_anagram(s1,s2)
            break

main()