# -*- coding = utf-8 -*-
# @Time    :$ {DATE}$ {TIME}
# @Author  :GT
# @File    :$ {DayDayUp01}.py

# [01] 365天，每天努力1%，天天向上，一年后努力是基数的多少倍，365天，每天下降1%，天天下降，一年后剩余的基数是多少倍
# 定义原始基数为1
dayup = 1
# 定义每天努力1%
dayfactor = 0.01
# 定义一年365天，每天努力基数+上1%，每天不努力，下降1%
dayup = pow(1+dayfactor, 365)
daydown = pow(1-dayfactor, 365)
#
print("平时向上努力，一年后是一年前的:{:.2f}倍\n平时向下下降，一年后剩余的是一年前的:{:.2f}倍".format(dayup, daydown))
# [02]工作日每天努力1%，一年后努力的是基数的多少倍
dayup = 1
for i in range(365):
    if i % 7 in [6, 0]:
        dayup = dayup * (1 - dayfactor)
    else:
        dayup = dayup * (1 + dayfactor)
print("工作日每天努力1%，一年后是一年前的:{:.2f}倍".format(dayup))

# [03]工作日每天努力多少，才可以达到天天努力的1%的倍数

def dayUP(df):
    dayup = 1
    for i in range(365):
        if i % 7 in [6, 0]:
            dayup = dayup*(1 - 0.01)
        else:
            dayup = dayup*(1 + df)
    return dayup


dayfactor = 0.01
while dayUP(dayfactor) < 37.78:
    dayfactor += 0.001
print("只在工作日努力，每天需要努力:{:.3f}，才可以在周六周日休息".format(dayfactor))


# 假如每天努力2小时，一年后努力了365*2=730小时，等于每年比别人多出60天






