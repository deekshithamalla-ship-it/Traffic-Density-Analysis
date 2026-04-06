import numpy as np
import csv 
import matplotlib.pyplot as plt

traffic_density=None
# function1 to enter data and save the data to the csv file
def enter_data():
    global traffic_density
    print("enter the traffic density day wise(24 hours)")
    data=[]
    for i in range(7):
        day=list(map(int,input(f"Day:{i+1}").split()))
        if len(day) != 24:
            print("Error: Enter exactly 24 values for each day.")
            return
        data.append(day)
    traffic_density=np.array(data)
    with open(r"traffic_density.csv",mode='w',newline='') as f:
        writer=csv.writer(f)
        header = ["Day"] + [f'hour {i}' for i in range(1,25)]
        writer.writerow(header)
        for i, row in enumerate(data):
            writer.writerow([f'Day {i+1}'] + row)
    print('data is entered')
def view_data():
    global traffic_density
    if traffic_density is None:
        print("data not available")
        return
    print("traffic data day wise(24 hrs)")
    print(traffic_density)
    print()
def analyze_data():
    if traffic_density is None:
        print("data not avilable")
        return
    total_traffic_day=traffic_density.sum(axis=1)
    avg_traffic_hour=traffic_density.mean(axis=0)
    # the axis=0 adds the colomns data and axis=1 adds row data
    for i,day in enumerate(total_traffic_day):
        print(f'Day {i+1}: {day}')
    for i,hour in enumerate(avg_traffic_hour):
        print(f'hour {i+1}: {hour}')
    print()
def peak_hour():
    if traffic_density is None:
        print("no data available")
        return
    avg_traffic_hour=traffic_density.mean(axis=0)
    max_peak=np.argmax(avg_traffic_hour)
    min_peak=np.argmin(avg_traffic_hour)
    print(f'max peak hour:{max_peak+1}({avg_traffic_hour[max_peak]})')
    print(f'min peak hour:{min_peak+1}({avg_traffic_hour[min_peak]})')
# function 5
def rank_day():
    total_traffic_day=traffic_density.sum(axis=1)
    rank_indices=np.argsort(-total_traffic_day)
    for i,r in enumerate(rank_indices):
        print(f'Rank {i+1}:Day {r+1} ({total_traffic_day[r]})')
    print()
 #function 6 to plot graphs
def plot_graph():
    day=[i for i in range(1,8)]
    total_traffic_day=traffic_density.sum(axis=1)
    plt.figure()
    plt.plot(day,total_traffic_day,marker='x',color='red')
    plt.title('day versus traffic density')
    plt.xlabel('day')
    plt.ylabel('traffic density')
    plt.show()
    hour=[i for i in range(1,25)]
    avg_traffic_hour=traffic_density.mean(axis=0)
    plt.figure()
    plt.plot(hour,avg_traffic_hour,marker='x',color='green')
    plt.title('hour versus traffic density')
    plt.xlabel('hour')
    plt.ylabel('avg traffic density')
    plt.show()

enter_data()
view_data()
analyze_data()
peak_hour()
rank_day()
plot_graph()



