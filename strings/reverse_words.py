# def reverse_words(s):
#     s.reverse()
#     def reverse_range(s,start,end):
#         while start < end:
#             s[start] , s[end] = s[end] , s[start]
#             start,end = start+1, end-1
#
#     start = 0
#     while True:
#         end = s.find(b' ',start)
#         if end<0:
#             break
#         reverse_range(s,start,end-1)
#     reverse_range(s,start,len(s)-1)
#
# print(reverse_words("Ram is a good boy"))

def reverse_words(s):
    arr = s.split(" ")
    print(" ".join(arr[::-1]))
reverse_words("Ram is a good boy")