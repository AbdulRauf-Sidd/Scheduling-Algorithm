class process:
	def __init__ (self, id, at, bt):
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
ready = []
for x in range(no):
	at = eval(input("Enter arrival time for proccess " + str(x) + ": "));
	bt = eval(input("Enter Burst Time for proccess " + str(x) + ": "));
	p = process(x, at, bt);
	ready.append(p);


#sort
for i in range(len(ready) - 1):
	for j in range(i + 1, len(ready)):
		if ready[i].at > ready[j].at:
			ready[i], ready[j] = ready[j], ready[i];

#check
for i in range(len(ready)):
	print(ready[i].at)

count = 0;
time = 0;
while count != no:
	process = ready[count];
	if (process.at <= time):
		time += process.bt;
		process.setct(time);
		count += 1;
	else:
		time += 1;


#Print Table
print("ID \tAT \tBT \tCT \tTAT \tWT");
totaltat = 0
totalwt = 0
for i in range(len(ready)):
	print(str(ready[i].id) + " \t" + str(ready[i].at) + " \t" + str(ready[i].bt) + " \t" +
	 str(ready[i].ct) + " \t" + str(ready[i].tat) + " \t" + str(ready[i].wt));
	totaltat += ready[i].tat;
	totalwt += ready[i].wt;
print("Average TAT: " + str(totaltat/no) + "\nAverage WT: " + str(totalwt/no))
