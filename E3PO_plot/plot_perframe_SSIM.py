import pandas as pd
import matplotlib.pyplot as plt
import json

with open("data/baseline/v3_s1_evaluation.json",'r') as f:
    json_data = json.load(f)
frame_result = json_data[:-1]
x1 = []
y1 = []
for frame in frame_result:
    x1.append(frame[0]['frame_idx'])
    y1.append(frame[0]['ssim'])
#print(y)

with open("data/cubemap/v3_s1_evaluation.json",'r') as f:
    json_data = json.load(f)
frame_result = json_data[:-1]
x2 = []
y2 = []
for frame in frame_result:
    x2.append(frame[0]['frame_idx'])
    y2.append(frame[0]['ssim'])


plt.plot(x1, y1, color='deepskyblue' ,marker='v', label='erp')
plt.plot(x2, y2, color='red' ,marker='v', label='cubemap')

# plt.title("PSNR vs Frame Number")
plt.xlabel("Frame Number")
plt.ylabel("SSIM (dB)")
plt.legend()
plt.grid(True)
plt.savefig('figs/ssim.png')
plt.show()
