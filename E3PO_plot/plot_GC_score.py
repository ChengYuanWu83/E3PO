import pandas as pd
import matplotlib.pyplot as plt
import json

x = []
y = []
apporach_folder = "cubemap"
for i in range(3, 4):
    with open("data/"+ apporach_folder +"/v"+ str(i) +"_s1_evaluation.json",'r') as f:
        json_data = json.load(f)
    final_result = json_data[-1]
    x.append("v"+ str(i) +"_s1")
    y.append(float(final_result['GC Score']))
    print(y)


plt.bar(x, y, color='deepskyblue')

# plt.title("PSNR vs Frame Number")
plt.gca().set_ylim([0, 10])
plt.xlabel("Video Number")
plt.ylabel("GC Score")
plt.xticks(x, x)

plt.show()
