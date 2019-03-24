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



