ifile<-read.table("mc1kTresults.txt")
df<-data.frame(ifile[order(ifile[,2], decreasing=T),1], 100*ifile[order(ifile[,2], decreasing=T),2]/sum(ifile[order(ifile[,2], decreasing=T),2]))
names(df)<-c("structure", "population")
svg("pops.svg", pointsize=5)
barplot(df[1:10,2], names.arg=df[1:10,1], ylim=c(0,40))
text(1:10, df[1:10,2], df[1:10,2])
dev.off()


