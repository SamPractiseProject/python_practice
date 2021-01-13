#tuple跟list差別在，tuple中的值不能更改



#自動打包，自動解包
#應用1
(one,two,three,four) = (1,2,3,4)
print(one)
print(two)
print(three)
print(four)
print('\n')
one1,two1,three1,four1=1,2,3,4
print(one1)
print(two1)
print(three1)
print(four1)

#應用2
a=3
b=4
print(a,b)
a,b=b,a
print(a,b)
print('\n')
#list和tuple轉換
print(list((1,2,3,4)))
print(tuple([1,2,3,4]))
print(list("HELLO"))
