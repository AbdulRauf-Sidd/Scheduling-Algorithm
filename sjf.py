class process:
	def __init__ (self, id, at, bt, pri):
		self.id = id;
		self.at = at;
		self.bt = bt;
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

#proccess details
total = []
for x in range(no):
	at = eval(input("Enter arrival time for proccess " + str(x) + ": "));
	bt = eval(input("Enter Burst Time for proccess " + str(x) + ": "));
	p = process(x, at, bt);
	total.append(p);

#AT sort
for i in range(len(total) - 1):
	for j in range(i + 1, len(total)):
		if total[i].at > total[j].at:
			total[i], total[j] = total[j], total[i];

def btsort(l):
	if len(l) > 1:
		for i in range(len(l) - 1):
			for j in range(i + 1, len(l)):
				if l[i].bt > l[j].bt:
					l[i], l[j] = l[j], l[i];
	return l;


#check
for i in range(len(total)):
	print(total[i].at)

count = 0;
time = 0;
ready = []
x = 0;
while count != no:
	#While there are processes left in total
	#Check which of the processes should be in ready at current time
	while (x != len(total)):
		if total[x].at <= time:
			ready.append(total[x]);
			x += 1;
		else:
			#remeber and continue from the index number in the next cycle
			break;

	if len(ready) > 0:
		#Sort According to BT
		ready = btsort(ready);
		#remove the shortest job from ready queue
		p = ready.pop(0);
		#add bt to total time, set ct of the completed process, and increment the completed process counter
		time += p.bt;
		p.setct(time);
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
