#Maintain an array of ten positive numbers. Initially all elements are set to zero
# (indicating array is empty). Write a menu driven program to perform operations like add number,
# delete number, find maximum number (along with its index), find minimum number (along with its index)
# and sum of numbers. While adding number display available indexes and user can select any of them.
# If no index is free, display appropriate message. Also, while deleting number display available indexes
# along with values and user can clear value there (set to zero).

def addnumber():
    a = int(input("Enter no you want to add"))
    array.append(a)
    print(array)


def deletenumber():
    b = int(input("Enter no you want to delete"))
    if b in array:
        array.remove(b)
        print(array)
    else:
        print("Entered Number is not Present in Array")

def maximumnumber():
    print("Maximum number from Array is ", max(array),"At index ", array.index(max(array)))

def minimumnumber():
    print("Minimum Number from Array is ", min(array), "At Index ", array.index(min(array)))

def sumofelements():
    print(sum(array))

array = []
for i in range(0, 10):
    n = int(input("Enter elements in Array"))
    array.append(n)
print(array)

opr = input("Select Operation you want to perform on Array\n1.Add Number\n2.Delete Number"
            "\n3.Maximum Number\n4.Minimum Number\n5.Sum of Numbers\n")
if opr == "Add Number":
    addnumber()

elif opr == "Delete Number":
    deletenumber()

elif opr == "Maximum Number":
    maximumnumber()

elif opr == "Minimum Number":
    minimumnumber()

elif opr == "Sum of Numbers":
    sumofelements()


