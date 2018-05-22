getwd()
setwd("C:/Work Space/R")
df <- read.csv("beat.csv")
summary(df)
df <- df[1:26,]
names(df) <-c("Country","Time","Spending","LE")
df$Spending <- as.numeric(as.character(df$Spending))
df$LE <- as.numeric(as.character(df$LE))
install.packages(c("car","rgl"))
install.packages("xtable")
library(car)
library(xtable)
library(rgl)
library(plotly)
library( Rcmdr)
myplot <- plot_ly(df, x = ~Time, y = ~Spending, z = ~LE, color =  df$Country)
rownames(df) <- df$Country
scatter3d(LE ~ Time + Spending,data = df, z = ,surface=TRUE, xlab = "Average time of doing physical activities (minutes)", ylab = "Spending per capita on sport and fitness (PPS)",
          zlab = "Life Expectancy (years)",axis.scales = TRUE ,axis.col = c("Red", "Blue", "Black"), labels = df$Country,labels = row.names(df), id.n=nrow(df))

scatter3d(x = df$Time, y = df$Spending, z = df$LE,surface=TRUE, xlab = "Average time of doing physical activities (minutes)", ylab = "Spending per capita on sport and fitness (PPS)",
          zlab = "Life Expectancy (years)",axis.scales = TRUE ,axis.col = c("Red", "Blue", "Black"), labels = row.names(df), id.n=nrow(df))

Identify3d(x = df$Time, y = df$Spending, z = df$LE)
