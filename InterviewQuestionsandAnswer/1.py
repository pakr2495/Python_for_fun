# def power(x,y):
#     if y<=1:
#         return x
#     else:
#         return x*power(x,y-1)





# def sumlist(li):
#     if not li:
#         return 0
#     else:
#         return li[0] + sumlist(li[1:])




# def fact(n):
#     if n<=1:
#         return 1
#     else:
#         return n*fact(n-1)



# def sumn(n):
#     if n==1:
#         return 1
#     else:
#         return n + sumn(n-1)



# def gcd(a,b):
#     if a == 0 or a == 1:
#         return b
#     if b ==1 or b == 0:
#         return a
#     if a>b:
#         return gcd(a%b,b)
#     else:
#         return gcd(a,b%a)

# #print(gcd(12,24))


# li = [1,2,3,4,5,6]
# for i in range(1,len(li)):
#     li[i] = li[i-1] + li[i]
# for i in range(1,len(li)):
#     li[i] = fact(li[i])

# #print(li)
arr = [1,4,2,5,3]
for i in range(1,len(arr)):
    arr[i] = arr[i-1] + arr[i]     
    sum_op = 0
for i in range(0,len(arr)-2):
    j = i+2
    while(j<=len(arr)-1):
        print(i,j)
        if i == 0:
            print(arr[j])
            sum_op = sum_op + arr[j]
        else:
            temp = arr[j] - arr[i-1]
            print(temp)
            sum_op = sum_op + temp
        j = j +2
print(sum_op + arr[len(arr)-1])


