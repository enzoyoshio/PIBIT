import matplotlib.pyplot as plt
import csv

fig, ax = plt.subplots(figsize=(20, 9))

handle = 'wallacebt'

x_axis = []
con_ids = []
ii = 1
with open('contests_ids.txt', 'r') as f:
	lines = f.readlines()
	for idx in lines:
		con_ids.append(idx.strip())
		x_axis.append(ii)
		ii += 1

y_axis = []

for idx in con_ids:
	with open('all_standings/' + str(idx) + '.csv', 'r') as f:
		reader = csv.reader(f)
		for row in reader:
			if row[1] == handle or row[2] == handle or row[3] == handle:
				y_axis.append(int(row[5][:-2]))
				break

# print(x_axis)
# print(y_axis)
# plot(x, y)
ax.plot(x_axis, y_axis)
ax.set_xlabel('contest_ID')
ax.set_ylabel(handle)
ax.set_title('graphic sample')
plt.show()
# ax.legend()
