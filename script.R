ref <- read.table("1_1.txt")
pdf(file="test.pdf")
plot(ref[,2:3])
dev.off()
