import statistics
import random
import plotly.figure_factory as ff
import pandas as pd
import plotly.graph_objects as go
import csv

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
mean1 = statistics.mean(data)
print("Mean of Sampling Data ->",mean1)

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0, counter):
        random_i = random.randint(0,len(data))
        value = data[random_i]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

mean_list =[]
for i in range(0,100):
    set_of_means = random_set_of_mean(30)
    mean_list.append(set_of_means)

def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df],["reading_time"], show_hist=False)
    fig.show()

std_deviation = statistics.stdev(mean_list)
print("The Standard Deviation of Sampling Distribution is -> " ,std_deviation)
mean = statistics.mean(mean_list)
print("The Mean of Sampling Distribution is -> ",mean)

first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)
print("std1",first_std_deviation_start,"," ,first_std_deviation_end)
print("std2", second_std_deviation_start,",",second_std_deviation_end)
print("std3", third_std_deviation_start,",",third_std_deviation_end)

fig = ff.create_distplot([mean_list],["reading_time"], show_hist = False)
fig.add_trace(go.Scatter(x=[mean,mean], y=[0,0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0,0.17], mode="lines", name="STANDARD DEVIATION START 1"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end], y=[0,0.17], mode="lines", name="STANDARD DEVIATION END 1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start,second_std_deviation_start], y=[0,0.17], mode="lines", name="STANDARD DEVIATION START 2"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0,0.17], mode="lines", name="STANDARD DEVIATION END 2"))
fig.add_trace(go.Scatter(x=[third_std_deviation_start, third_std_deviation_start], y=[0,0.17], mode="lines", name="STANDARD DEVIATION  START 3"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end,second_std_deviation_end], y=[0,0.17], mode="lines", name="STANDARD DEVIATION END 3"))
fig.show()

z_score = (mean - mean1)/std_deviation
print("The Z score is ->" ,z_score)