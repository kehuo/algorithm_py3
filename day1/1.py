'''https://www.nowcoder.com/test/question/3897c2bcc87943ed98d8e0b9e18c4666?pid=260145&tid=22525465
老师想知道从某某同学当中，分数最高的是多少，现在请你编程模拟老师的询问。当然，老师有时候需要更新某位同学的成绩.

输入描述:
输入包括多组测试数据。
每组输入第一行是两个正整数N和M（0 < N <= 30000,0 < M < 5000）,分别代表学生的数目和操作的数目。
学生ID编号从1编到N。
第二行包含N个整数，代表这N个学生的初始成绩，其中第i个数代表ID为i的学生的成绩
接下来又M行，每一行有一个字符C（只取‘Q’或‘U’），和两个正整数A,B,当C为'Q'的时候, 表示这是一条询问操作，他询问ID从A到B（包括A,B）的学生当中，成绩最高的是多少
当C为‘U’的时候，表示这是一条更新操作，要求把ID为A的学生的成绩更改为B。

输出描述:
对于每一次询问操作，在一行里面输出最高成绩.
'''

s_number,op_times=map(int,input('学生数和操作次数分别为: ').split())
init_score=list(map(int,input('初始成绩: ').split()))
if len(init_score)==s_number:
	print('学生数量: ',s_number)
	print('操作次数: ',op_times)
	print('初始成绩: ',init_score)

	#if s_number>0 and s_number<=30000 and op_times>0 and op_times<5000:
	op_report=[]
	while op_times>0:
		op=list(map(str,input('输入操作类型(Q为查询，U为输入)和查询参数A和B: ').split()))
			#目前op= ['U', '1', '48']
		op[1]=int(op[1])
		op[2]=int(op[2])
		print(op)
			#print(isinstance(op[1],int))
		op_times=op_times-1
		op_report.append(op)

	print(op_report)

	i=1
	while i<=len(op_report):
		comp1=init_score[op_report[i-1][1]-1]
		comp2=init_score[op_report[i-1][2]-1]
		res=max(comp1,comp2)
		i=i+1
		print(res)




	#else:
	#	print('wrong number')
else:
	print('学生数量是和成绩的数量不一致，请再次输入')



