# -*- coding: utf-8 -*-

print('hello python!')

# IF 语句的基本语法

a=88

if a>=0:
    print('yes')
else:
    print('no')    


print("双引号")   

print('单引号')    

print('''三引号''')    

print('aaw"fasd')
print("aaw'fasd")
print('''aaw'fasd''')


# 整数

int1 = 1 + 1

int2 = 3 - 4
# python 2.7 得出的结果是0 3.x 是0.5
int3 = 1 / 2

print(int1)
print(int2)
print(int3)

print(type(int3))

print(0.55 + 0.41)

print(0.55 + 0.4)

print(0.55 + 0.411)


# list Python 内置的一种有序集合数据类型

### 定义
name = ['张三','李四','陈五','王刘','马七']

### 读取
print(name[0])
print(name[0:2])
print(name[:])

### 修改
name[1] = 'laozhang'

print(name)

name.append('追加')

print(name)

### 删除

del name[3]

print(name)

### list 运算符

#### 长度

len(name)

max(name)
min(name)

## list(tuple) 元组转换成list


#### 衔接

[1,2,3] + [4,5.6]

#### 复制
['复制我把！']*5

#### 是否存在

3 in [1,2,3,4]

#### 迭代
for x in [7,8,9,1,2,3]: 
     
      print(x)


#### 99乘法表

for i in range(1,10):

    for j in range(1,i+1):

        print('{}X{}={}\t'.format(i,j,i*j),end="")

    print()


       
    
