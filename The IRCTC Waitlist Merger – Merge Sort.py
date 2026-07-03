"""IRCTC maintains two separately sorted waiting lists: One from the mobile app. One from railway reservation counters. Instead of sorting all passengers again, IRCTC combines both sorted lists into one final sorted waiting list. Write a program to merge the two sorted waiting lists using the merge step of Merge Sort."""
l1 = [2, 5, 8, 10]
l2 = [1, 4, 6, 9]
result = []

i = 0
j = 0

while i < len(l1) and j < len(l2):

    if l1[i] < l2[j]:
        result.append(l1[i])
        i += 1

    else:
        result.append(l2[j])
        j += 1

while i < len(l1):
    result.append(l1[i])
    i += 1

while j < len(l2):
    result.append(l2[j])
    j += 1

print("Merged List:",result)
