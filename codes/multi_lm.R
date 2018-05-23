data=read.table("boston.csv",sep=",")[,2:15]
lm_boston <- lm(data[,14]~data[,1]+data[,2]+data[,3]+data[,4]
	+data[,5]+data[,6]+data[,7]+data[,8]+data[,9]+
	data[,10]+data[,11]+data[,12]+data[,13])
print(summary(lm_boston))
b=step(lm_boston, direction = "backward", trace=FALSE )
print(b)