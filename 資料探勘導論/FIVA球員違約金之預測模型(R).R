#匯入csv檔
library(readr)
fifa_data <- read_csv("C:/Users/lruri/Dropbox/PC/Downloads/fifa_data.csv")

#重新命名欄位並選擇所需之欄位建立資料集(df)
names(fifa_data)[57]<-"Release_Clause"
names(fifa_data)[10]<-"Preferred_Foot"
names(fifa_data)[14]<-"Work_Rate"
df <- subset(fifa_data, select = c(Age, Stamina, Aggression, Preferred_Foot, Work_Rate, Wage, Release_Clause))
str(df)

#Part1:資料處理

df$Work_Rate<- sub("/.*", "", df$Work_Rate)
df$Wage <- gsub("[€KM]", "", df$Wage)
df$Wage <- as.numeric(df$Wage)

df$Release_Clause <- gsub("[€KM]", "", df$Release_Clause)
df$Release_Clause <- as.numeric(df$Release_Clause)
df$Release_Clause <- ifelse(grepl("M", fifa_data$Release_Clause), df$Release_Clause * 1000, df$Release_Clause)
df$Release_Clause <- as.numeric(df$Release_Clause)

#處理NA值
table(is.na(df))

mean_value<-mean(df$Stamina, na.rm = TRUE)
df[which(is.na(df[,"Stamina"])), "Stamina"] <- mean_value

mean_value<-mean(df$Aggression, na.rm=TRUE)
df[which(is.na(df[,"Aggression"])), "Aggression"] <- mean_value

df<-na.omit(df)

table(is.na(df$Stamina))
table(is.na(df$Aggression))
table(is.na(df))

##Part2:繪圖找出關聯性
require(ggplot2)
require(lattice)
#1散布圖
ggplot(data=df) +     
  geom_point(aes(x=Aggression,           
                 y=Stamina)) +
  theme_bw() 


#2散布圖
plot(x=df$Wage, y=df$Release_Clause,pch=16)
d1 <- df[df$Preferred_Foot=="Right", ]
points(x=d1$Wage, y=d1$Release_Clause,pch=16, col="green")
d2 <- df[df$Preferred_Foot=="Left", ]
points(x=d2$Wage, y=d2$Release_Clause,pch=16, col="red")
legend("topleft", pch=16,
       legend=c("Right","Left"), 
       col=c("red", "green")
)

#3盒鬚圖
qplot(x=Wage,      
      y=Release_Clause, 
      data=df, 
      geom="boxplot",    # graph type is boxplot
      color=Work_Rate)

#Part3:迴歸分析
mod <- lm(formula= Release_Clause ~ Wage + Age + Stamina,
            data=df)
summary(mod)

#殘差(residual)是否符合三個假設:
#常態性(Normality)
#獨立性(Independence)
#變異數同質性(Homogeneity of Variance)
require(car)

#常態性(Normality)
#虛無假設H0:殘差服從常態分配
#母體太大，隨機抽樣取500個樣本
set.seed(123)
sampled_data <- sample(mod$residual, size = 500)
shapiro.test(sampled_data) 

#獨立性(Independence)
#虛無假設H0:殘差間相互獨立
durbinWatsonTest(mod) 

#變異數同質性(Homogeneity of Variance)
#虛無假設H0:殘差變異數具有同質性
ncvTest(mod) 

#預測
new.df <- data.frame(Wage=64, Age=24, Stamina=84)
new.df
predict(mod, new.df)

#變異數分析(ANOVA)Release_Clause有所差異
#H0:μ(Right)=μ(Left)
R.lm <- lm(Release_Clause~Preferred_Foot, data=df)
anova(R.lm)
L.lm <- lm(Release_Clause~Preferred_Foot, data=df)
anova(L.lm)


#vif解釋變數之間相關程度
vif(mod)

