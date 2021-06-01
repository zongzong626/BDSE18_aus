packages = c("jiebaR", "tm", "tmcn", "dplyr", "tidytext", "ggplot2", "wordcloud2", "rvest","stringr","dygraphs","knitr")
existing = as.character(installed.packages()[,1])
for(pkg in packages[!(packages %in% existing)]) install.packages(pkg)
#載入packages
library(rvest)
library(httr)
library(jiebaR)
library(tm)
library(tmcn)
library(dplyr)
library(tidytext)
library(stringr)
library(ggplot2)
library(dygraphs)
library(wordcloud2)
library(knitr)
library(kableExtra)
library(RColorBrewer)
library(wordcloud2)
library(Rtsne)

#改板名跟頁數
all_url_page = paste0('https://www.ptt.cc/bbs/Aussiekiwi/index',1:99,'.html') 
all_url_data = c(); recom=c(); title=c(); date=c()
for(i in 1:length(all_url_page)){
  all_url_data = c(all_url_data, read_html (all_url_page[i]) %>% 
                     html_nodes(css = ".title a") %>% html_attr('href'))
  recom = c(recom,read_html(all_url_page[i]) %>% html_nodes(css = ".nrec") %>% html_text())
  title = c(title, read_html(all_url_page[i]) %>% html_nodes(css = ".title a") %>% html_text())
  date = c(date, read_html(all_url_page[i]) %>% html_nodes(css = ".date") %>% html_text())
  if(i %% 30 == 0) Sys.sleep(runif(1,2,5))
}

my_data<- data.frame(recom,date,title)
all_url_data<- paste0('https://www.ptt.cc',all_url_data)
content=c()

for(i in 1:length(all_url_data)){
  tryCatch({content <- c(content,read_html(all_url_data[i]) %>% html_nodes(css = "#main-content") %>% html_text())
  if(i %% 30 == 0) Sys.sleep(runif(1,2,5))
  cat(i,"\n")},error=function(err){
    message("Original error message:",i)
    message(paste0(err,"\n"))
    return(i=i+1)}
  )}

my_data <- cbind(my_data,data.frame(content=content[1:1980]))
#去頭去尾
content_ques <- my_data$content %>% gsub(pattern = "作者.+:[0-9]{2}\\s[0-9]{4}?",., replacement = "") %>% 
gsub(pattern = "(\n--\n※).+",., replacement = "")
#整理內文  
content_ques <- content_ques %>%
  gsub(pattern = "(http|https)://[a-zA-Z0-9./?=_-]+",., replacement = "") %>% #去除網頁
  gsub(pattern = "引述《[a-zA-Z0-9./_()].+》之銘言",., replacement = "") %>% #去除引述
  gsub(pattern = "Sent from [a-zA-Z0-9 -./_()]+",., replacement = "") %>% #去除Sent from
  gsub(pattern = "<U[a-zA-Z0-9 +]+>",., replacement = "") %>% #去除光碟
  gsub(pattern = "[0-9]{4}/[0-9]{2}/[0-9]{2}",., replacement = "") %>% #去除日期格式:2020/01/16
  gsub(pattern = "[0-9]{4}-[0-9]{2}-[0-9]{2}",., replacement = "") %>% #去除日期格式:2020-01-16
  gsub(pattern = "[0-9]{4}年[0-9]{1,2}月[0-9]{1,2}日",., replacement = "") %>% #去除日期格式:2020年1月16日
  gsub(pattern = "[0-9]{1,2}/[0-9]{1,2}",., replacement = "") %>% #去除日期格式:01/22
  gsub(pattern = "[0-9]{1,2}-[0-9]{1,2}",., replacement = "") %>% #去除日期格式:01-22
  gsub(pattern = "[0-9]{1,2}月[0-9]{1,2}日",., replacement = "") %>% #去除日期格式:01月22日
  gsub(pattern = "[0-9]{2}:[0-9]{2}",., replacement = "") %>% #去除時間
  gsub(pattern = "新聞網址",., replacement = "") %>% 
  gsub(pattern = "\n",., replacement = "") %>% # 清理斷行符號
  gsub(pattern = "[/_.★↑｜▲△～─→──┐─╱┘●※]+?",.,replacement = "")

content_ques = removePunctuation (content_ques,ucp=T) #去除全形標點符號
content_ques = removePunctuation(content_ques) #去除半形標點符號
content_ques = stripWhitespace(content_ques) #去除空白

my_data = cbind(my_data,content_ques) 
#整理標題
title_clear <-  my_data$title %>%
  gsub(pattern = "\\[.+?\\]",., replacement = "") %>% 
  gsub(pattern = "Fw",., replacement = "") %>%
  gsub(pattern = "Re",., replacement = "") %>% 
  gsub(pattern = "[0-9]{1,2}/[0-9]{1,2}",., replacement = "") %>%
  gsub(pattern = "[0-9]{2}:[0-9]{2}",., replacement = "") %>%
  removePunctuation (.,ucp=T) %>% 
  stripWhitespace() 

my_data = cbind(my_data,title_clear)
#資料預覽
#kable(head(my_data)) %>% kable_styling(bootstrap_options = c("striped", "hover", "condensed", "responsive")) %>% scroll_box(height="200px")
#回覆內文數>>42
length(grep("Re:", my_data$title))
#轉發內文數>>44
length(grep("Fw:", my_data$title))
#標題類型個數
title_1 <- regmatches(my_data$title,regexec(pattern = "\\[.+?\\]",my_data$title))
title_topic=c()
for(i in 1:1980){
  title_topic <- c(title_topic,title_1[[i]])
}
title_topic <- title_topic %>% gsub(pattern = " ",., replacement = "") 
title_topic <- as.factor(title_topic)
sort(summary(title_topic), decreasing = TRUE)
write.csv(my_data,file="C:/data/aus_travel_1_99.csv")

####################################################################################################################################################
###合併所有csv檔###
# install.packages("plyr")
library(plyr)
# 設定資料夾位置
setwd("C:/data/aus_travel")
# 將資料夾中的csv檔合在一起
dataset <- ldply(list.files(), read.csv, header=F)
# 匯出csv檔
write.csv(dataset,file="aus_travel_merge.csv")
