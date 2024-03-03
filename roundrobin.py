class process:
	def __init__ (self, id, at, bt):
		self.id = id;
		self.at = at;
		self.bt = bt;
		self.rt = bt;
		self.ct = None;
		self.tat = None;
		self.wt = None;

	def setct(self, x):
		self.ct = x;
		self.settat();
		self.setwt();

	def settat(self):
		self.tat = self.ct - self.at;

	def setwt(self):
		self.wt = self.tat - self.bt;


no = eval(input("Enter number of processes: "));
qt = eval(input("Enter Quantum time: "));

#proccess details
total = []
for x in range(no):
	at = eval(input("Enter arrival time for process " + str(x) + ": "));
	bt = eval(input("Enter Burst Time for process " + str(x) + ": "));
	p = process(x, at, bt);
	total.append(p);

#AT sort
for i in range(len(total) - 1):
	for j in range(i + 1, len(total)):
		if total[i].at > total[j].at:
			total[i], total[j] = total[j], total[i];


#check
for i in range(len(total)):
	print(total[i].at)

count = 0;
time = 0;
ready = [];
qtp = 0;
x = 0;
while count != no:
	#While there are processes left in total
	#Check which of the processes should be in ready at current time
	while (x != len(total)):
		if total[x].at <= time:
			ready.append(total[x]);
			x += 1;
		else:
			break;
			#remeber and continue from the index number in the next cycle
	if len(ready) > 0:
		process = ready[0];
		#remove from the front ofthe queue
		ready.pop(0)
		#check if quantum time is less than remaning time of the current process
		if qt < process.rt:
			process.rt -= qt;
			time += qt;
			#Update Ready Queue
			while (x!= len(total)):
				if total[x].at <= time:
					ready.append(total[x]);
					x += 1;
				else:
					break;
			ready.append(process);
			#put at the end of the queue
		else:
			time += process.rt;
			process.setct(time);
			count += 1;
	else:
		#Increase time by 1
		time +=1

#print ct
print("ID \tAT \tBT \tCT \tTAT \tWT");
totaltat = 0
totalwt = 0
for i in range(len(total)):
	print(str(total[i].id) + " \t" + str(total[i].at) + " \t" + str(total[i].bt) + " \t" + str(total[i].ct) +
	" \t" + str(total[i].tat) + " \t" + str(total[i].wt));
	totaltat += total[i].tat;
	totalwt += total[i].wt;
print("Average TAT: " + str(totaltat/no) + "\nAverage WT: " + str(totalwt/no));
