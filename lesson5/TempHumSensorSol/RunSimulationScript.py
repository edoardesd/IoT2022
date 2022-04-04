print "********************************************";
print "*                                          *";
print "*             TOSSIM Script                *";
print "*                                          *";
print "********************************************";

import sys;
import time;

from TOSSIM import *;

t = Tossim([]);

t = Tossim([]);


topofile="topology.txt";
modelfile="meyer-heavy.txt";


print "Initializing mac....";
mac = t.mac();
print "Initializing radio channels....";
radio=t.radio();
print "    using topology file:",topofile;
print "    using noise file:",modelfile;
print "Initializing simulator....";
t.init();


out = sys.stdout;

#Add debug channel
print "Activate debug message on channel boot"
t.addChannel("boot",out);
print "Activate debug message on channel temp"
t.addChannel("temp",out);
print "Activate debug message on channel hum"
t.addChannel("hum",out);
print "Activate debug message on channel timer"
t.addChannel("timer",out);
print "Activate debug message on channel radio"
t.addChannel("radio",out);
print "Activate debug message on channel radio_pack"
t.addChannel("radio_pack",out);
print "Activate debug message on channel radio_send"
t.addChannel("radio_send",out);
print "Activate debug message on channel radio_rec"
t.addChannel("radio_rec",out);

#Create nodes

#Create node 1
print "Creating node 0 (master)"
node0 =t.getNode(0);
time0 = 0*t.ticksPerSecond();
node0.bootAtTime(time0);
print ">>>Node 0 boots at time",  time0/t.ticksPerSecond(), "[sec]";

#Create node 2
print "Creating node 1"
node1 =t.getNode(1);
time1 = 0*t.ticksPerSecond();
node1.bootAtTime(time1);
print ">>>Node 1 boots at time",  time1/t.ticksPerSecond(), "[sec]";

#Create node 3
print "Creating node 2"
node2 =t.getNode(2);
time2 = 5*t.ticksPerSecond();
node2.bootAtTime(time2);
print ">>>Node 2 boots at time",  time2/t.ticksPerSecond(), "[sec]";


print "Creating radio channels..."
f = open(topofile, "r");
lines = f.readlines()
for line in lines:
  s = line.split()
  if (len(s) > 0):
    print ">>>Setting radio channel from node ", s[0], " to node ", s[1], " with gain ", s[2], " dBm"
    radio.add(int(s[0]), int(s[1]), float(s[2]))


#creation of channel model
print "Initializing Closest Pattern Matching (CPM)...";
noise = open(modelfile, "r")
lines = noise.readlines()
compl = 0;
mid_compl = 0;

print "Reading noise model data file:", modelfile;
print "Loading:",
for line in lines:
    str = line.strip()
    if (str != "") and ( compl < 10000 ):
        val = int(str)
        mid_compl = mid_compl + 1;
        if ( mid_compl > 5000 ):
            compl = compl + mid_compl;
            mid_compl = 0;
            sys.stdout.write ("#")
            sys.stdout.flush()
        for i in range(0, 3):
            t.getNode(i).addNoiseTraceReading(val)
print "Done!";

for i in range(0, 3):
    print ">>>Creating noise model for node:",i;
    t.getNode(i).createNoiseModel()

print "Start simulation with TOSSIM! \n\n\n";

for i in range(0,1000):
	t.runNextEvent()
	
print "\n\n\nSimulation finished!";

