print 'Simulator starts'

from pprint import pprint
import os
import sys
if len(sys.argv) != 6:
    print ('Usage: simulator.py inst.txt data.txt reg.txt config.txt result.txt')
    os._exit(1)

ins = sys.argv[1]
data = sys.argv[2]
reg = sys.argv[3]
config = sys.argv[4]
result = sys.argv[5]

# Read the instruction and store the instruction in a list of [block,address,instruction,access_bit]


f = open(ins, 'r')
lbl_list=[]
label_list=[]
block=0
addr=0
acc_bit=0
i=0
instruction = []
for l in f:
    if ':' in l:
        divide=l.strip().split(':')
        div=divide[0].strip()
        lbl_list.append(div)    
    if ',' in l:
        part=l.strip().split(',')
        part1=part[1].strip()
        partition=part[0].strip().split()
        if '(' in part1:
            reg_offset=part1.strip().split('(')
            offset=reg_offset[0]
            ld_rg=reg_offset[1].strip().split(')')
            load_reg=ld_rg[0]
            if offset.isdigit()==False:
                print 'inst error. offset invalid'
                os._exit(1)

            load_reg=load_reg.upper()
            if len(load_reg)>3:
                print 'inst error. load/store register is invalid 1'
                os._exit(1)
            if(load_reg[0]!='R'):
                print 'inst error. load/store register is invalid 2'
                os._exit(1)
            if len(load_reg)<3:
                if(load_reg[1].isdigit()==False):
                    print 'inst error. load/store register is invalid 3'
                    os._exit(1)
            elif len(load_reg)==3:
                load_num=load_reg[1]+load_reg[2]
                if(load_num.isdigit()==False or int(load_num)<0 or int(load_num)>31):
                    print 'inst error. load/store register is invalid 4'
                    os._exit(1)
               
        # When label is present in instruction
        if len(partition)>2:
            labl= partition[0].strip()
            lb=labl.strip().split(':')
            label_list.append(lb[0])
            opcode=partition[1].strip()
            dest=partition[2].strip()
            labl=labl.upper()
            if(labl[-1]!=':'):
                print 'inst error.Label error'
                os._exit(1)
                
            #VALIDATE OPCODE
            opcode=opcode.strip().upper()
            if (opcode== 'LW' or opcode== 'SW' or opcode== 'L.D'
                or opcode== 'S.D' or opcode== 'DADD' or opcode== 'DADDI'
                or opcode== 'DSUB' or opcode== 'DSUBI' or opcode== 'AND'
                or opcode== 'ANDI' or opcode== 'OR' or opcode== 'ORI'
                or opcode== 'ADD.D' or opcode== 'MUL.D' or opcode== 'DIV.D'
                or opcode== 'SUB.D' or opcode== 'BNE' or opcode== 'BEQ'
                or opcode== 'HLT' or opcode== 'J'):
                print
            else:
                print 'inst error. opcode error'
                os._exit(1)
                
            #VALIDATE DESTINATION
            dest=dest.upper()
            if len(dest)>3:
                print 'inst error. dest is invalid 1'
                os._exit(1)
            if(dest[0]=='R' or dest[0]=='F'):
                print 
            else:
                print 'inst error. dest is invalid 2'
                os._exit(1)
            if len(dest)<3:
                if(dest[1].isdigit()==False):
                    print 'inst error. dest is invalid 3'
                    os._exit(1)
            elif len(dest)<4:
                dest_num=dest[1]+dest[2]
                print dest_num
                if(dest_num.isdigit()==False or int(dest_num)<0 or int(dest_num)>31):
                    print 'inst error. dest is invalid '
                    os._exit(1)
            
            # when label is followed by arithmetic/logical operation
            if len(part)>2:
                source1=part[1].strip()
                source2=part[2].strip()

                source1=source1.upper()
                if len(source1)>3:
                    print 'inst error. source1 is invalid 1'
                    os._exit(1)
                if(source1[0]=='R' or source1[0]=='F'):
                    print
                else:
                    print 'inst error. source1 is invalid 2'
                    os._exit(1)
                if len(source1)<3:
                    if(source1[1].isdigit()==False):
                        print 'inst error. source1 is invalid 3'
                        os._exit(1)
                elif len(source1)<4:
                    src_num=source1[1]+source1[2]
                    if(src_num.isdigit()==False or int(src_num)<0 or int(src_num)>31):
                        print 'inst error. source1 is invalid 4'
                        os._exit(1)


                source2=source2.upper()
                if(source2.isdigit()==True):
                    print 
                if(source2.isdigit()==False):
                    if len(source2)>3:
                        if(source2[0]!='R' and source2[0]!='F'):
                            if source2 in label_list:
                                print source2
                        else:
                            print 'inst error. source2 is invalid 1'
                            os._exit(1)
                    if len(source2)>1 and len(source2)<3:
                        if(source2[0]=='R' or source2[0]=='F'):
                            if(source2[1].isdigit()==False):
                                print 'inst error. source2 is invalid 2'
                                os._exit(1)
                            else:
                                print
                        elif(source2[0]!='R' and source2[0]!='F'):
                            if source2 in label_list:
                                print
                            elif source2[0]=='-' and source2[1].isdigit()==True:
                                print 
                            else:
                                print 'inst error. source2 is invalid 3'
                                os._exit(1)
                        else:
                            print 'inst error. source2 is invalid 5'
                            os._exit(1)
                    elif len(source2)==3:
                        src_num=source2[1]+source2[2]
                        if(src_num.isdigit()==False or int(src_num)<0 or int(src_num)>31):
                            print 'inst error. source2 is invalid 6'
                            os._exit(1)
                    else:
                        print 'inst error. source2 is invalid 7'
                        os._exit(1)
                        
            # when label is followed by load/store operation
            else:
                source=load_reg
                #VALIDATE SOURCE
                if len(source)>3:
                    print 'inst error. load/store register invalid 1'
                    os._exit(1)
                if(source[0]!='R'):
                    print 'inst error. load/store register invalid 2'
                    os._exit(1)
                if len(source)<3:
                    if(source[1].isdigit()==False):
                        print 'inst error. load/store register invalid 3'
                        os._exit(1)
                elif len(source)==3:
                    src_num=source[1]+source[2]
                    if(src_num.isdigit()==False or int(src_num)<0 or int(src_num)>31):
                        print 'inst error. load/store register is invalid 4'
                        os._exit(1)
        # When label is not present in instruction
        # Arithmetic/Logical operations without label
        if len(partition)<3 and len(part)>2:
            opcode=partition[0].strip()
            dest=partition[1].strip()
            source1=part[1].strip()
            source2=part[2].strip()
            opcode=opcode.strip().upper()
            if (opcode== 'LW' or opcode== 'SW' or opcode== 'L.D'
                or opcode== 'S.D' or opcode== 'DADD' or opcode== 'DADDI'
                or opcode== 'DSUB' or opcode== 'DSUBI' or opcode== 'AND'
                or opcode== 'ANDI' or opcode== 'OR' or opcode== 'ORI'
                or opcode== 'ADD.D' or opcode== 'MUL.D' or opcode== 'DIV.D'
                or opcode== 'SUB.D'or opcode== 'BNE' or opcode== 'BEQ'
                or opcode== 'HLT' or opcode== 'J'):
                print
            else:
                print 'inst error. opcode invalid'
                os._exit(1)
            #VALIDATE DESTINATION
            dest=dest.upper()
            if len(dest)>3:
                print 'inst error. non label dest is invalid 1'
                os._exit(1)
            if(dest[0]=='R' or dest[0]=='F'):
                print 
            else:
                print 'inst error. non label dest is invalid 2'
                os._exit(1)
            if len(dest)<3:
                if(dest[1].isdigit()==False):
                    print 'inst error. non label dest is invalid 3'
                    os._exit(1)
            elif len(dest)<4:
                dest_num=dest[1]+dest[2]
                print dest_num
                if(dest_num.isdigit()==False or int(dest_num)<0 or int(dest_num)>31):
                    print 'inst error. non label dest is invalid '
                    os._exit(1)
            
            #VALIDATE SOURCE 1 AND 2
            source1=part[1].strip()
            source2=part[2].strip()

            source1=source1.upper()
            if len(source1)>3:
                print 'inst error. non label source1 is invalid 1'
                os._exit(1)
            if(source1[0]=='R' or source1[0]=='F'):
                print
            else:
                print 'inst error. non label source1 is invalid 2'
                os._exit(1)
            if len(source1)<3:
                if(source1[1].isdigit()==False):
                    print 'inst error. non label source1 is invalid 3'
                    os._exit(1)
            elif len(source1)<4:
                src_num=source1[1]+source1[2]
                if(src_num.isdigit()==False or int(src_num)<0 or int(src_num)>31):
                    print 'inst error. non label source1 is invalid 4'
                    os._exit(1)


            source2=source2.upper()
            if(source2.isdigit()==True):
                print 
            if(source2.isdigit()==False):
                if len(source2)>3:
                    if(source2[0]!='R' and source2[0]!='F'):
                        if source2 in label_list:
                            print source2
                    else:
                        print 'inst error. non label source2 is invalid 1'
                        os._exit(1)
                if len(source2)>1 and len(source2)<3:
                    if(source2[0]=='R' or source2[0]=='F'):
                        if(source2[1].isdigit()==False):
                            print 'inst error. non label source2 is invalid 2'
                            os._exit(1)
                        else:
                            print
                    elif(source2[0]!='R' and source2[0]!='F'):
                        if source2 in lbl_list:
                            print
                        elif source2[0]=='-' and source2[1].isdigit()==True:
                            print 
                        else:
                            print 'inst error. non label source2 is invalid 3'
                            os._exit(1)
                    else:
                        print 'inst error. non label source2 is invalid 5'
                        os._exit(1)
                elif len(source2)==3:
                    src_num=source2[1]+source2[2]
                    if(src_num.isdigit()==False or int(src_num)<0 or int(src_num)>31):
                        print 'inst error. non label source2 is invalid 6'
                        os._exit(1)
                else:
                    print 'inst error. non label source2 is invalid 7'
                    os._exit(1)

        #Load/store operation without label
        elif len(partition)<3 and len(part)<3:
            opcode=partition[0].strip()
            dest=partition[1].strip()
            source=load_reg
            opcode=opcode.strip().upper()
            if (opcode== 'LW' or opcode== 'SW' or opcode== 'L.D'
                or opcode== 'S.D' or opcode== 'DADD' or opcode== 'DADDI'
                or opcode== 'DSUB' or opcode== 'DSUBI' or opcode== 'AND'
                or opcode== 'ANDI' or opcode== 'OR' or opcode== 'ORI'
                or opcode== 'ADD.D' or opcode== 'MUL.D' or opcode== 'DIV.D'
                or opcode== 'SUB.D'or opcode== 'BNE' or opcode== 'BEQ'
                or opcode== 'HLT' or opcode== 'J'):
                print
            else:
                print 'inst error. non label l/s opcode invalid'
                os._exit(1)
            
            #VALIDATE DESTINATION
            dest=dest.upper()
            if len(dest)>3:
                print 'inst error. non label l/s dest is invalid 1'
                os._exit(1)
            if(dest[0]=='R' or dest[0]=='F'):
                print 
            else:
                print 'inst error. non label l/s dest is invalid 2'
                os._exit(1)
            if len(dest)<3:
                if(dest[1].isdigit()==False):
                    print 'inst error. non label l/s dest is invalid 3'
                    os._exit(1)
            elif len(dest)<4:
                dest_num=dest[1]+dest[2]
                print dest_num
                if(dest_num.isdigit()==False or int(dest_num)<0 or int(dest_num)>31):
                    print 'inst error. non label l/s dest is invalid '
                    os._exit(1)
            
            #VALIDATE SOURCE
                if len(source)>3:
                    print 'inst error. non label load/store register invalid 1'
                    os._exit(1)
                if(source[0]!='R'):
                    print 'inst error. non label load/store register invalid 2'
                    os._exit(1)
                if len(source)<3:
                    if(source[1].isdigit()==False):
                        print 'inst error. non label load/store register invalid 3'
                        os._exit(1)
                elif len(source)==3:
                    src_num=source[1]+source[2]
                    if(src_num.isdigit()==False or int(src_num)<0 or int(src_num)>31):
                        print 'inst error. non label load/store register is invalid 4'
                        os._exit(1)
    if ',' not in l:
        part=l.strip().split()
        if len(part)>1:
            jmp_label=part[1].strip()
            if part[0].upper()=='J':
                for k, v in label_store.items():
                    if k==jmp_label:
                        print
                    else:
                        print' inst error. branch inst invalid'
                        os._exit(1)
        else:
            if(part[0].upper()=='HLT'):
                print
            else:
                print 'inst error. unknown operation. (Expected HLT)'
                os._exit(1)


    tempInst = []
    tempInst.append(block)
    i +=1
    if (i % 4 == 0):
        block = block + 1
    tempInst.append(hex(addr))
    tempInst.append(l.strip().upper())
    tempInst.append(acc_bit)
    instruction.append(tempInst)
    addr=addr + 4
print 'INSTRUCTIONS'
pprint(instruction)

                

# Store the labels in a dictionary of [label_name, value]

label_store= {}
for l in instruction:
    if ':' in l[2]:
        divide = l[2].strip().split(':')
        label_value=divide[0].strip()
        label_store[label_value]=l[1]

print 'LABELS'
pprint(label_store)

        
# Read the data file and store the data in a list of [block,address,data,access_bit,modify_bit]

f1 = open(data,'r')
data=[]
block=0
addr= 256
acc_bit=0
mod_bit=0
i=0
for l in f1:
    tempInst =[]
    tempInst.append(block)
    i += 1
    if (i % 4 == 0):
        block += 1
    tempInst.append(hex(addr))
    addr=addr+ 4
    d=l.strip()
    dt=int(d,2)
    dat=bin(dt)
    tempInst.append(dat)
    tempInst.append(acc_bit)
    tempInst.append(mod_bit)
    data.append(tempInst)

print 'DATA'
pprint (data)

# Read the Register.txt file and store the registers in a dictionary of {Reg_no, value}

f2=open(reg,'r')
register = {}
i=0;
for l in f2:
    register['R'+ str(i)]=l.strip()
    i += 1
for k,v in register.items():
    register[k]=bin(int(v,2))
print 'REGISTER'
pprint (register)

# Read the config.txt file and store the registers in a dictionary of {config_label, config_value}

f3 = open(config,'r')
config = {}

for l in f3:
    if ':' in l:
        divide = l.strip().split(':')
        part1=divide[0].strip().upper()
        part2=divide[1].strip()
        if (part1.upper()=='FP ADDER' or part1.upper()=='FP MULTIPLIER'
            or part1.upper()=='FP DIVIDER' or part1.upper()=='I-CACHE'
            or part1.upper()=='D-CACHE' or part1.upper()=='MAIN MEMORY'):
            print
        else:
            print 'config title error'
            os._exit(1)
        partition=part2.strip().split(',')
        if partition[0]=='':
            print 'config Missing value in config'
            os._exit(1)
        time=partition[0].strip()
        if len(time)>1:
            for t in time:
                if(t.isdigit()!=True):
                    print'config error. clk_cyc is not correct'
                    os._exit(1)
        if len(time)<2:
           if(time[0].isdigit()!=True):
               print'config error. clk_cyc is not correct'
               os._exit(1)
        if(part1=='MAIN MEMORY' or part1=='I-CACHE' or part1=='D-CACHE'):
            if partition[0].isdigit()!=True:
                print 'config error. only clock cycles required for memory and cache'
                os._exit(1)
        if len(partition)>1:
            pipe=partition[1].strip().lower()
        if(pipe.strip()=='yes' or pipe.strip()=='no'):
           print
        else:
           print 'config error. mention pipelined or not properly'
           os._exit(1)

        divide = l.strip().split(':')
        config_label=divide[0].strip().upper()
        config_value=divide[1].strip()
    config[config_label]=config_value

print 'CONFIG'
pprint (config)
print 


#Populate Instruction cache

fo = open(result, 'w')
fo.write('Instruction\t\t\t\t\t\tIF\t\tID\t\tEX\t\tWB\t\tRAW\t\tWAR\t\tWAW\t\tSTRUCT \n')
    
instruction_cache= [[],[],[],[]]
pc=0
data_cache=[[[],[]],[[],[]]]
T=int(config['MAIN MEMORY'])
k=int(config['I-CACHE'])
#print instruction_cache
counter=0

cc_if = 0
if_list=[]
cc_id=0
id_list=[]
cc_ex=0
ex_list=[]
cc_wb=0
wb_list=[]
cc_dc=0
dc_list=[]

ex1_list=[]
dst_list=[]
if1_list=[]

source_list=[]
dest_list=[]
raw_hazard=[]
waw_hazard=[]
struct_hazard=[]

ic_access=0
dc_access=0
ic_hit=0
dc_hit=0

while pc < 256 :
    T=int(config['MAIN MEMORY'])
    k=int(config['I-CACHE'])
    flag = False
    if instruction_cache==[[],[],[],[]]:
        cc_if = cc_if +(2*(T+k))
        for id in id_list:
            if ',' not in id:
                clk=int(id)
                if (clk>cc_if+1):
                    cc_if=clk
        ic_access+=1
        for l in instruction:
            if(l[1]==hex(pc)):
                b = l[0]
        for i in instruction:
            if i[0]==b:
                mod_block=i[0] % 4
                instruction_cache[mod_block].append(i)
                for blk in instruction_cache:
                    for ins in blk:
                        if(ins[1]==hex(pc)):
                            fetch_inst=ins[2]
                            
    else:
        for blk in instruction_cache:
            for ins in blk:
                if(ins[1]==hex(pc)):
                    cc_if +=1
                    fetch_inst=ins[2]
                    ic_access+=1
                    ic_hit+=1
                    for id in id_list:
                        if ',' not in id:
                            clk=int(id)
                            if (clk>cc_if):
                                cc_if=clk
                    flag = True
                    
               
        if flag == False:
            for m in instruction:
                if(m[1]==hex(pc)):
                    bl = m[0]
                    cc_if = cc_if +(2*(T+k))
                    for id in id_list:
                        if ',' not in id:
                            clk=int(id)
                            if (clk>cc_if):
                                cc_if=clk
                    ic_access+=1
            for some in instruction:
                if some[0]==bl:
                    mod_block= some[0]%4
                    instruction_cache[mod_block].append(some)
                    for blk in instruction_cache:
                        for ins in blk:
                            if(ins[1]==hex(pc)):
                                fetch_inst=ins[2]
                                
    temp=[]
    temp.append(fetch_inst)
    temp.append(cc_if)
    if_list.extend(temp)
    temp1=[]
    temp1.append(fetch_inst)
    temp1.append(str(cc_if))
    if1_list.append(temp1)
    print 'pc %s' % (pc)
    pc=pc+4

    
    #print 'if_list is %s' % (if_list)
    #print
    print "INSTRUCTION CACHE "
##    pprint (instruction_cache[0])
##    #print
##    pprint (instruction_cache[1])
##    #print
##    pprint (instruction_cache[2])
##    #print
##    pprint (instruction_cache[3])
    print
    print 'fetch %s' % (fetch_inst)
    print 'cc_if %s' % (cc_if)
    #print
    #print 'IF LIST'
    #pprint(if_list)

    # Instruction decode stage

    #print
    #print 'Instruction: %s' % (fetch_inst)
    if ',' in fetch_inst:
        part=fetch_inst.strip().split(',')
        #print 'All parts: %s' % (part)
        #print 'part 0: %s' % (part[0].strip())
        #print 'part 1: %s' % (part[1].strip())
        part1=part[1].strip()
        partition=part[0].strip().split()

        # check for registers in insttruction (load doesnt have part[2])
        #if len(part) > 2:
        #print 'part 2: %s' %(part[2].strip())
            #print 'partition 0: %s' % (partition[0].strip())
            #print 'partition 1: %s' % (partition[1].strip())

        # Separate the offset and register for load and store
        if '(' in part1:
            reg_offset=part1.strip().split('(')
            offset=reg_offset[0]
            ld_rg=reg_offset[1].strip().split(')')
            load_reg=ld_rg[0]
            print 'offset is %s and load register is %s' %(offset,load_reg)
            #print 'load register is %s' % (load_reg)

        # When label is present in instruction
        if len(partition)>2:
            #print 'partition 2: %s' % (partition[2].strip())
            #print

        # check for the opcode, source and destination registers
            label= partition[0].strip()
            opcode=partition[1].strip()
            dest=partition[2].strip()
            print "label is %s" % (label)
            print "opcode is %s" % (opcode)
            
            # when label is followed by arithmetic/logical operation
            if len(part)>2:
                source1=part[1].strip()
                source2=part[2].strip()
                print "source 1 is %s" % (source1)
                print "source 2 is %s" % (source2)
                temp2=[]
                temp2.append(source1)
                temp2.append(source2)
                source_list.extend(temp2)
                
            # when label is followed by load/store operation
            else:
                source=load_reg
                print "source is %s" % (source)
                print "offset is %s" % (offset)
                temp2=[]
                temp2.append(source)
                source_list.extend(temp2)
                
            print "dest is %s" % (dest)

        # When label is not present in instruction
        # Arithmetic/Logical operations without label
        if len(partition)<3 and len(part)>2:
            opcode=partition[0].strip()
            dest=partition[1].strip()
            print
            print "opcode is %s" % (opcode)
            source1=part[1].strip()
            source2=part[2].strip()
            print "source 1 is %s" % (source1)
            print "source 2 is %s" % (source2)
            print "dest is %s" % (dest)
            temp2=[]
            temp2.append(source1)
            temp2.append(source2)
            source_list.extend(temp2)
        #Load/store operation without label
        elif len(partition)<3 and len(part)<3:
            opcode=partition[0].strip()
            dest=partition[1].strip()
            print
            print "opcode is %s" % (opcode)
            source=load_reg
            print "source is %s" % (source)
            print "offset is %s" % (offset)
            print "dest is %s" % (dest)
            temp2=[]
            temp2.append(source)
            source_list.extend(temp2)
            
        # Do opcode comparisions to figure out the operation
        opcode=opcode.strip().upper()
        raw_temp=[]
        raw_temp.append(fetch_inst)
        raw_temp.append('N')
        raw_hazard.extend(raw_temp)

        waw_temp=[]
        waw_temp.append(fetch_inst)
        waw_temp.append('N')
        waw_hazard.extend(waw_temp)

        struct_temp=[]
        struct_temp.append(fetch_inst)
        struct_temp.append('N')
        struct_hazard.extend(struct_temp)


        if opcode.strip().upper()=='LW':
            cc_id=cc_if+1
            #Check for RAW Hazard
            for dst in dst_list:
                if source==dst[0]:
                    dst_clk=dst[1]
                    if(cc_id < dst_clk):
                        cc_id=dst_clk
                        raw_hazard.pop()
                        raw_hazard.pop()
                        raw_temp=[]
                        raw_temp.append(fetch_inst)
                        raw_temp.append('Y')
                        raw_hazard.extend(raw_temp)

            for dst in dst_list:
                if dest==dst[0]:
                    dst_clk=dst[1]
                    d_wb=wb_list[-1]
                    if(d_wb < dst_clk):
                        wb_list.pop()
                        wb_list.append(dst_clk)
                        waw_hazard.pop()
                        waw_hazard.pop()
                        waw_temp=[]
                        waw_temp.append(fetch_inst)
                        waw_temp.append('Y')
                        waw_hazard.extend(waw_temp)
##            #Check for RAW Hazard
##            
##            for dst in dest_list:
##                if source==dst:
##                    dst_index=dest_list.index(dst)
##                    if(cc_id < dest_list[dst_index+1]):
##                        cc_id=dest_list[dst_index+1]
##                        raw_hazard.pop()
##                        raw_hazard.pop()
##                        raw_temp=[]
##                        raw_temp.append(fetch_inst)
##                        raw_temp.append('Y')
##                        raw_hazard.extend(raw_temp)
##            #Check for WAW Hazard
##            for dst in dest_list:
##                if dest==dst:
##                    dst_index=dest_list.index(dst)
##                    d_wb=wb_list[-1]
##                    if(d_wb < dest_list[dst_index+1]):
##                        wb_list.pop()
##                        wb_list.append(dest_list[dst_index+1]+1)
##                        waw_hazard.pop()
##                        waw_hazard.pop()
##                        waw_temp=[]
##                        waw_temp.append(fetch_inst)
##                        waw_temp.append('Y')
##                        waw_hazard.extend(waw_temp)

            id_list.append(fetch_inst)
            id_list.append(str(cc_id))
            for key, value in register.items():
                if key==source:
                    src_ld=int(value,2)
                    print 'source LW %s is %s' % (source,src_ld)

        if opcode.strip().upper()=='SW':
            cc_id=cc_if+1
            s=source
            d=dest
            source=d
            dest=s
            #Check for RAW Hazard
            for dst in dest_list:
                if source==dst:
                    dst_index=dest_list.index(dst)
                    if(cc_id < dest_list[dst_index+1]):
                        cc_id=dest_list[dst_index+1]
                        raw_hazard.pop()
                        raw_hazard.pop()
                        raw_temp=[]
                        raw_temp.append(fetch_inst)
                        raw_temp.append('Y')
                        raw_hazard.extend(raw_temp)
            temp=[]
            temp.append(fetch_inst)
            temp.append(str(cc_id))
            id_list.extend(temp)
            for key, value in register.items():
                if key==source:
                    src_st=int(value,2)
                    print 'source SW %s is %s' % (source,src_st)
                if key==dest:
                    dst_st=int(value,2)
                    print 'dest SW %s is %s' %(dest, dst_st)
                    
        if opcode.strip().upper()=='L.D':
            cc_id=cc_if+1
            #Check for RAW Hazard
            for dst in dst_list:
                if source==dst[0]:
                    dst_clk=dst[1]
                    if(cc_id < dst_clk):
                        cc_id=dst_clk
                        raw_hazard.pop()
                        raw_hazard.pop()
                        raw_temp=[]
                        raw_temp.append(fetch_inst)
                        raw_temp.append('Y')
                        raw_hazard.extend(raw_temp)

            for dst in dst_list:
                if dest==dst[0]:
                    dst_clk=dst[1]
                    d_wb=wb_list[-1]
                    if(d_wb < dst_clk):
                        wb_list.pop()
                        wb_list.append(dst_clk)
                        waw_hazard.pop()
                        waw_hazard.pop()
                        waw_temp=[]
                        waw_temp.append(fetch_inst)
                        waw_temp.append('Y')
                        waw_hazard.extend(waw_temp)
            temp=[]
            temp.append(fetch_inst)
            temp.append(str(cc_id))
            id_list.extend(temp)
                
            for key, value in register.items():
                if key==source:
                    src_ld=int(value,2)
                    print 'source L.D %s is %s' % (source,src_ld)

        if opcode.strip().upper()=='S.D':
            cc_id=cc_if+1
            s=source
            d=dest
            source=d
            dest=s
            #Check for RAW Hazard
            for dst in dst_list:
                if source==dst[0]:
                    dst_clk=dst[1]
                    if(cc_id < dst_clk):
                        cc_id=dst_clk
                        raw_hazard.pop()
                        raw_hazard.pop()
                        raw_temp=[]
                        raw_temp.append(fetch_inst)
                        raw_temp.append('Y')
                        raw_hazard.extend(raw_temp)
            temp=[]
            temp.append(fetch_inst)
            temp.append(str(cc_id))
            id_list.extend(temp)
            
            for key, value in register.items():
                if key==source:
                    src_st=int(value,2)
                    print 'source S.D %s is %s' % (source,src_st)
                if key==dest:
                    dst_st=int(value,2)
                    print 'dest S.d %s is %s' %(dest, dst_st)

        if opcode.strip().upper()=='DADD':
            cc_id=cc_if+1
            #Check for RAW Hazard
            dst_clk1=0
            dst_clk2=0
            for dst in dst_list:
                if source1==dst[0]:
                    dst_clk1= int(dst[1])
                if source2==dst[0]:
                    dst_clk2=int(dst[1])
                if(cc_id < max(dst_clk1,dst_clk2)):
                    cc_id = max(dst_clk1,dst_clk2)
                    raw_hazard.pop()
                    raw_hazard.pop()
                    raw_temp=[]
                    raw_temp.append(fetch_inst)
                    raw_temp.append('Y')
                    raw_hazard.extend(raw_temp)
            #Check for waw hazard        
            for dst in dst_list:
                if dest==dst[0]:
                    dst_clk=int(dst[1])
                    d_wb=wb_list[-1]
                    if(d_wb < dst_clk):
                        wb_list.pop()
                        wb_list.append(dst_clk+1)
                        waw_hazard.pop()
                        waw_hazard.pop()
                        waw_temp=[]
                        waw_temp.append(fetch_inst)
                        waw_temp.append('Y')
                        waw_hazard.extend(waw_temp)
##            #Check for RAW Hazard
##            dst_clk1=0
##            dst_clk2=0
##            for dst in dest_list:
##                if source1==dst:
##                    dst_index1=dest_list.index(dst)
##                    dst_clk1=dest_list[dst_index1+1]
##                if source2==dst:
##                    dst_index2=dest_list.index(dst)
##                    dst_clk2=dest_list[dst_index2+1]
##                if(cc_id < max(dst_clk1,dst_clk2)):
##                    cc_id = max(dst_clk1,dst_clk2)
##                    raw_hazard.pop()
##                    raw_hazard.pop()
##                    raw_temp=[]
##                    raw_temp.append(fetch_inst)
##                    raw_temp.append('Y')
##                    raw_hazard.extend(raw_temp)
##            #Check for WAW Hazard
##            for dst in dest_list:
##                if dest==dst:
##                    dst_index=dest_list.index(dst)
##                    d_wb=wb_list[-1]
##                    if(d_wb < dest_list[dst_index+1]):
##                        wb_list.pop()
##                        wb_list.append(dest_list[dst_index+1]+1)
##                        waw_hazard.pop()
##                        waw_hazard.pop()
##                        waw_temp=[]
##                        waw_temp.append(fetch_inst)
##                        waw_temp.append('Y')
##                        waw_hazard.extend(waw_temp)
            temp=[]
            temp.append(fetch_inst)
            temp.append(str(cc_id))
            id_list.extend(temp)
            for key, value in register.items():
                if key==source1:
                    src1=int(value,2)
                    print 'source1 DADD is %s' % (src1)
                if key==source2:
                    src2=int(value,2)
                    print 'source2 DADD is %s' % (src2)

        if opcode.strip().upper()=='DADDI':
            cc_id=cc_if+1
            #Check for RAW Hazard
            dst_clk1=0
            dst_clk2=0
            for dst in dst_list:
                if source1==dst[0]:
                    dst_clk1= int(dst[1])
                if source2==dst[0]:
                    dst_clk2=int(dst[1])
                if(cc_id < max(dst_clk1,dst_clk2)):
                    cc_id = max(dst_clk1,dst_clk2)
                    raw_hazard.pop()
                    raw_hazard.pop()
                    raw_temp=[]
                    raw_temp.append(fetch_inst)
                    raw_temp.append('Y')
                    raw_hazard.extend(raw_temp)
            #Check for waw hazard        
            for dst in dst_list:
                if dest==dst[0]:
                    dst_clk=int(dst[1])
                    d_wb=wb_list[-1]
                    if(d_wb < dst_clk):
                        wb_list.pop()
                        wb_list.append(dst_clk+1)
                        waw_hazard.pop()
                        waw_hazard.pop()
                        waw_temp=[]
                        waw_temp.append(fetch_inst)
                        waw_temp.append('Y')
                        waw_hazard.extend(waw_temp)
            temp=[]
            temp.append(fetch_inst)
            temp.append(str(cc_id))
            id_list.extend(temp)
            
            for key, value in register.items():
                if key==source1:
                    src1=int(value,2)
                    print 'source1 DADDI is %s' % (src1)
            src2=int(source2)
            print 'source2 DADDI is %s' % (src2)

        if opcode.strip().upper()=='DSUB':
            cc_id=cc_if+1
            #Check for RAW Hazard
            dst_clk1=0
            dst_clk2=0
            for dst in dst_list:
                if source1==dst[0]:
                    dst_clk1= int(dst[1])
                if source2==dst[0]:
                    dst_clk2=int(dst[1])
                if(cc_id < max(dst_clk1,dst_clk2)):
                    cc_id = max(dst_clk1,dst_clk2)
                    raw_hazard.pop()
                    raw_hazard.pop()
                    raw_temp=[]
                    raw_temp.append(fetch_inst)
                    raw_temp.append('Y')
                    raw_hazard.extend(raw_temp)
            #Check for waw hazard        
            for dst in dst_list:
                if dest==dst[0]:
                    dst_clk=int(dst[1])
                    d_wb=wb_list[-1]
                    if(d_wb < dst_clk):
                        wb_list.pop()
                        wb_list.append(dst_clk+1)
                        waw_hazard.pop()
                        waw_hazard.pop()
                        waw_temp=[]
                        waw_temp.append(fetch_inst)
                        waw_temp.append('Y')
                        waw_hazard.extend(waw_temp)
            temp=[]
            temp.append(fetch_inst)
            temp.append(str(cc_id))
            id_list.extend(temp)
            
            for key, value in register.items():
                if key==source1:
                    src1=int(value,2)
                    print 'source1 DSUB is %s' % (src1)
                if key==source2:
                    src2=int(value,2)
                    print 'source2 DSUB is %s' % (src2)
        if opcode.strip().upper()=='DSUBI':
            cc_id=cc_if+1
           #Check for RAW Hazard
            dst_clk1=0
            dst_clk2=0
            for dst in dst_list:
                if source1==dst[0]:
                    dst_clk1= int(dst[1])
                if source2==dst[0]:
                    dst_clk2=int(dst[1])
                if(cc_id < max(dst_clk1,dst_clk2)):
                    cc_id = max(dst_clk1,dst_clk2)
                    raw_hazard.pop()
                    raw_hazard.pop()
                    raw_temp=[]
                    raw_temp.append(fetch_inst)
                    raw_temp.append('Y')
                    raw_hazard.extend(raw_temp)
            #Check for waw hazard        
            for dst in dst_list:
                if dest==dst[0]:
                    dst_clk=int(dst[1])
                    d_wb=wb_list[-1]
                    if(d_wb < dst_clk):
                        wb_list.pop()
                        wb_list.append(dst_clk+1)
                        waw_hazard.pop()
                        waw_hazard.pop()
                        waw_temp=[]
                        waw_temp.append(fetch_inst)
                        waw_temp.append('Y')
                        waw_hazard.extend(waw_temp)
            temp=[]
            temp.append(fetch_inst)
            temp.append(str(cc_id))
            id_list.extend(temp)
            
            for key, value in register.items():
                if key==source1:
                    src1=int(value,2)
                    print 'source1 DSUBI is %s' % (src1)
            src2=int(source2)
            print 'source2 DSUBI is %s' % (src2)

        if opcode.strip().upper()=='AND':
            cc_id=cc_if+1
            #Check for RAW Hazard
            dst_clk1=0
            dst_clk2=0
            for dst in dst_list:
                if source1==dst[0]:
                    dst_clk1= int(dst[1])
                if source2==dst[0]:
                    dst_clk2=int(dst[1])
                if(cc_id < max(dst_clk1,dst_clk2)):
                    cc_id = max(dst_clk1,dst_clk2)
                    raw_hazard.pop()
                    raw_hazard.pop()
                    raw_temp=[]
                    raw_temp.append(fetch_inst)
                    raw_temp.append('Y')
                    raw_hazard.extend(raw_temp)
            #Check for waw hazard        
            for dst in dst_list:
                if dest==dst[0]:
                    dst_clk=int(dst[1])
                    d_wb=wb_list[-1]
                    if(d_wb < dst_clk):
                        wb_list.pop()
                        wb_list.append(dst_clk+1)
                        waw_hazard.pop()
                        waw_hazard.pop()
                        waw_temp=[]
                        waw_temp.append(fetch_inst)
                        waw_temp.append('Y')
                        waw_hazard.extend(waw_temp)
            temp=[]
            temp.append(fetch_inst)
            temp.append(str(cc_id))
            id_list.extend(temp)
            
            for key, value in register.items():
                if key==source1:
                    src1=int(value,2)
                    print 'source1 OR is %s' % (src1)
                if key==source2:
                    src2=int(value,2)
                    print 'source2 OR is %s' % (src2)
                    
        if opcode.strip().upper()=='ANDI':
            cc_id=cc_if+1
           #Check for RAW Hazard
            dst_clk1=0
            dst_clk2=0
            for dst in dst_list:
                if source1==dst[0]:
                    dst_clk1= int(dst[1])
                if source2==dst[0]:
                    dst_clk2=int(dst[1])
                if(cc_id < max(dst_clk1,dst_clk2)):
                    cc_id = max(dst_clk1,dst_clk2)
                    raw_hazard.pop()
                    raw_hazard.pop()
                    raw_temp=[]
                    raw_temp.append(fetch_inst)
                    raw_temp.append('Y')
                    raw_hazard.extend(raw_temp)
            #Check for waw hazard        
            for dst in dst_list:
                if dest==dst[0]:
                    dst_clk=int(dst[1])
                    d_wb=wb_list[-1]
                    if(d_wb < dst_clk):
                        wb_list.pop()
                        wb_list.append(dst_clk+1)
                        waw_hazard.pop()
                        waw_hazard.pop()
                        waw_temp=[]
                        waw_temp.append(fetch_inst)
                        waw_temp.append('Y')
                        waw_hazard.extend(waw_temp)
            temp=[]
            temp.append(fetch_inst)
            temp.append(str(cc_id))
            id_list.extend(temp)
            
            for key, value in register.items():
                if key==source1:
                    src1=int(value,2)
                    print 'source1 ANDI is %s' % (src1)
            src2=int(source2)
            print 'source2 ANDI is %s' % (source2)
        if opcode.strip().upper()=='OR':
            cc_id=cc_if+1
            #Check for RAW Hazard
            dst_clk1=0
            dst_clk2=0
            for dst in dst_list:
                if source1==dst[0]:
                    dst_clk1= int(dst[1])
                if source2==dst[0]:
                    dst_clk2=int(dst[1])
                if(cc_id < max(dst_clk1,dst_clk2)):
                    cc_id = max(dst_clk1,dst_clk2)
                    raw_hazard.pop()
                    raw_hazard.pop()
                    raw_temp=[]
                    raw_temp.append(fetch_inst)
                    raw_temp.append('Y')
                    raw_hazard.extend(raw_temp)
            #Check for waw hazard        
            for dst in dst_list:
                if dest==dst[0]:
                    dst_clk=int(dst[1])
                    d_wb=wb_list[-1]
                    if(d_wb < dst_clk):
                        wb_list.pop()
                        wb_list.append(dst_clk+1)
                        waw_hazard.pop()
                        waw_hazard.pop()
                        waw_temp=[]
                        waw_temp.append(fetch_inst)
                        waw_temp.append('Y')
                        waw_hazard.extend(waw_temp)
            temp=[]
            temp.append(fetch_inst)
            temp.append(str(cc_id))
            
            for key, value in register.items():
                if key==source1:
                    src1=int(value,2)
                    print 'source1 OR is %s' % (src1)
                if key==source2:
                    src2=int(value,2)
                    print 'source2 OR is %s' % (src2)

        if opcode.strip().upper()=='ORI':
            cc_id=cc_if+1
            #Check for RAW Hazard
            dst_clk1=0
            dst_clk2=0
            for dst in dst_list:
                if source1==dst[0]:
                    dst_clk1= int(dst[1])
                if source2==dst[0]:
                    dst_clk2=int(dst[1])
                if(cc_id < max(dst_clk1,dst_clk2)):
                    cc_id = max(dst_clk1,dst_clk2)
                    raw_hazard.pop()
                    raw_hazard.pop()
                    raw_temp=[]
                    raw_temp.append(fetch_inst)
                    raw_temp.append('Y')
                    raw_hazard.extend(raw_temp)
            #Check for waw hazard        
            for dst in dst_list:
                if dest==dst[0]:
                    dst_clk=int(dst[1])
                    d_wb=wb_list[-1]
                    if(d_wb < dst_clk):
                        wb_list.pop()
                        wb_list.append(dst_clk+1)
                        waw_hazard.pop()
                        waw_hazard.pop()
                        waw_temp=[]
                        waw_temp.append(fetch_inst)
                        waw_temp.append('Y')
                        waw_hazard.extend(waw_temp)
            temp=[]
            temp.append(fetch_inst)
            temp.append(str(cc_id))
            id_list.extend(temp)
            
            for key, value in register.items():
                if key==source1:
                    src1=int(value,2)
                    print 'source1 ORI is %s' % (src1)
            src2=int(source2) 
            print 'source2 ORI is %s' % (src2)

        if opcode.strip().upper()=='ADD.D':
            cc_id=cc_if+1
            #Check for RAW Hazard
            dst_clk1=0
            dst_clk2=0
            for dst in dst_list:
                if source1==dst[0]:
                    dst_clk1= int(dst[1])
                if source2==dst[0]:
                    dst_clk2=int(dst[1])
                if(cc_id < max(dst_clk1,dst_clk2)):
                    cc_id = max(dst_clk1,dst_clk2)
                    raw_hazard.pop()
                    raw_hazard.pop()
                    raw_temp=[]
                    raw_temp.append(fetch_inst)
                    raw_temp.append('Y')
                    raw_hazard.extend(raw_temp)
                    
            for dst in dst_list:
                if dest==dst[0]:
                    dst_clk=int(dst[1])
                    d_wb=wb_list[-1]
                    if(d_wb < dst_clk):
                        wb_list.pop()
                        wb_list.append(dst_clk+1)
                        waw_hazard.pop()
                        waw_hazard.pop()
                        waw_temp=[]
                        waw_temp.append(fetch_inst)
                        waw_temp.append('Y')
                        waw_hazard.extend(waw_temp)
            temp=[]
            temp.append(fetch_inst)
            temp.append(str(cc_id))
            id_list.extend(temp)
            
            for key, value in register.items():
                if key==source1:
                    src1=int(value,2)
                    print 'source1 ADD.D is %s' % (src1)
                if key==source2:
                    src2=int(value,2)
                    print 'source2 ADD.D is %s' % (src2)
        if opcode.strip().upper()=='MUL.D':
            cc_id=cc_if+1
            #Check for RAW Hazard
            dst_clk1=0
            dst_clk2=0
            for dst in dst_list:
                if source1==dst[0]:
                    dst_clk1= int(dst[1])
                if source2==dst[0]:
                    dst_clk2=int(dst[1])
                if(cc_id < max(dst_clk1,dst_clk2)):
                    cc_id = max(dst_clk1,dst_clk2)
                    raw_hazard.pop()
                    raw_hazard.pop()
                    raw_temp=[]
                    raw_temp.append(fetch_inst)
                    raw_temp.append('Y')
                    raw_hazard.extend(raw_temp)
                    
            for dst in dst_list:
                if dest==dst[0]:
                    dst_clk=int(dst[1])
                    d_wb=wb_list[-1]
                    if(d_wb < dst_clk):
                        wb_list.pop()
                        wb_list.append(dst_clk+1)
                        waw_hazard.pop()
                        waw_hazard.pop()
                        waw_temp=[]
                        waw_temp.append(fetch_inst)
                        waw_temp.append('Y')
                        waw_hazard.extend(waw_temp)
            temp=[]
            temp.append(fetch_inst)
            temp.append(str(cc_id))
            id_list.extend(temp)
            
            for key, value in register.items():
                if key==source1:
                    src1=int(value,2)
                    print 'source1 MUL.D is %s' % (src1)
                if key==source2:
                    src2=int(value,2)
                    print 'source2 MUL.D is %s' % (src2)

        if opcode.strip().upper()=='DIV.D':
            cc_id=cc_if+1
            #Check for RAW Hazard
            dst_clk1=0
            dst_clk2=0
            for dst in dst_list:
                if source1==dst[0]:
                    dst_clk1= int(dst[1])
                if source2==dst[0]:
                    dst_clk2=int(dst[1])
                if(cc_id < max(dst_clk1,dst_clk2)):
                    cc_id = max(dst_clk1,dst_clk2)
                    raw_hazard.pop()
                    raw_hazard.pop()
                    raw_temp=[]
                    raw_temp.append(fetch_inst)
                    raw_temp.append('Y')
                    raw_hazard.extend(raw_temp)
                    
            for dst in dst_list:
                if dest==dst[0]:
                    dst_clk=int(dst[1])
                    d_wb=wb_list[-1]
                    if(d_wb < dst_clk):
                        wb_list.pop()
                        wb_list.append(dst_clk+1)
                        waw_hazard.pop()
                        waw_hazard.pop()
                        waw_temp=[]
                        waw_temp.append(fetch_inst)
                        waw_temp.append('Y')
                        waw_hazard.extend(waw_temp)
            temp=[]
            temp.append(fetch_inst)
            temp.append(str(cc_id))
            id_list.extend(temp)
            
            for key, value in register.items():
                if key==source1:
                    src1=int(value,2)
                    print 'source1 DIV.D is %s' % (src1)
                if key==source2:
                    src2=int(value,2)
                    print 'source2 DIV.D is %s' % (src2)
        if opcode.strip().upper()=='SUB.D':
            cc_id=cc_if+1
            #Check for RAW Hazard
            dst_clk1=0
            dst_clk2=0
            for dst in dst_list:
                if source1==dst[0]:
                    dst_clk1= int(dst[1])
                if source2==dst[0]:
                    dst_clk2=int(dst[1])
                if(cc_id < max(dst_clk1,dst_clk2)):
                    cc_id = max(dst_clk1,dst_clk2)
                    raw_hazard.pop()
                    raw_hazard.pop()
                    raw_temp=[]
                    raw_temp.append(fetch_inst)
                    raw_temp.append('Y')
                    raw_hazard.extend(raw_temp)
            #Check for waw hazard        
            for dst in dst_list:
                if dest==dst[0]:
                    dst_clk=int(dst[1])
                    d_wb=wb_list[-1]
                    if(d_wb < dst_clk):
                        wb_list.pop()
                        wb_list.append(dst_clk+1)
                        waw_hazard.pop()
                        waw_hazard.pop()
                        waw_temp=[]
                        waw_temp.append(fetch_inst)
                        waw_temp.append('Y')
                        waw_hazard.extend(waw_temp)
            temp=[]
            temp.append(fetch_inst)
            temp.append(str(cc_id))
            id_list.extend(temp)
            
            for key, value in register.items():
                if key==source1:
                    src1=int(value,2)
                    print 'source1 SUB.D is %s' % (src1)
                if key==source2:
                    src2=int(value,2)
                    print 'source2 DADD is %s' % (src2)

        # Branch equations finish in ID stage and loop is true
        if opcode.strip().upper()=='BEQ':
            cc_id=cc_if+1
            l=source2
            s2=source1
            s1=dest
            source1=s1
            source2=s2
            branch_label=l
            #Check for RAW Hazard
            dst_clk1=0
            dst_clk2=0
            for dst in dst_list:
                if source1==dst[0]:
                    dst_clk1= int(dst[1])
                if source2==dst[0]:
                    dst_clk2=int(dst[1])
                if(cc_id < max(dst_clk1,dst_clk2)):
                    cc_id = max(dst_clk1,dst_clk2)
                    raw_hazard.pop()
                    raw_hazard.pop()
                    raw_temp=[]
                    raw_temp.append(fetch_inst)
                    raw_temp.append('Y')
                    raw_hazard.extend(raw_temp)
            temp=[]
            temp.append(fetch_inst)
            temp.append(str(cc_id))
            id_list.extend(temp)
            
            for key, value in register.items():
                if key==source1:
                    print 'source1 BEQ is %s %s' % (source1, register[source1])
                if key==source2:
                    print 'source2 BEQ is %s %s' % (source2,register[source2])
                if register[source1]==register[source2]:
                    for k, v in label_store.items():
                       if k==branch_label:
                           pc=int(v,16)
                           cc_ex=''
                           cc_wb=''
                           continue
            print hex(pc)
        if opcode.strip().upper()=='BNE':
            cc_id=cc_if+1
            l=source2
            s2=source1
            s1=dest
            source1=s1
            source2=s2
            branch_label=l
            #Check for RAW Hazard
            dst_clk1=0
            dst_clk2=0
            for dst in dst_list:
                if source1==dst[0]:
                    dst_clk1= int(dst[1])
                if source2==dst[0]:
                    dst_clk2=int(dst[1])
                if(cc_id < max(dst_clk1,dst_clk2)):
                    cc_id = max(dst_clk1,dst_clk2)
                    raw_hazard.pop()
                    raw_hazard.pop()
                    raw_temp=[]
                    raw_temp.append(fetch_inst)
                    raw_temp.append('Y')
                    raw_hazard.extend(raw_temp)
            temp=[]
            temp.append(fetch_inst)
            temp.append(str(cc_id))
            id_list.extend(temp)
            
            for key, value in register.items():
                if key==source1:
                    print 'source1 BNE is %s %s' % (source1, register[source1])
                if key==source2:
                    print 'source2 BNE is %s %s' % (source2,register[source2])
                if register[source1]!=register[source2]:
                    for k, v in label_store.items():
                       if k==branch_label:
                           pc=int(v,16)
                           cc_wb=''
                           cc_ex=''
                           continue
                
        
    # check for halt and jump doesnt contain ',' 
    if ',' not in fetch_inst:
        part=fetch_inst.strip().split()
        if len(part)>1:
            jmp_label=part[1].strip().upper()
            print 'label is %s ' %(jmp_label)
            if part[0].upper()=='J':
                cc_id=cc_if+1
                temp=[]
                temp.append(fetch_inst)
                temp.append(str(cc_id))
                id_list.extend(temp)    
                for k, v in label_store.items():
                    if k==jmp_label:
                        pc=v
                        cc_wb=''
                        cc_ex=''
                        continue
        else:
            part[0].upper()=='HLT'
            cc_id=cc_if+1
            temp=[]
            temp.append(fetch_inst)
            temp.append(str(cc_id))
            id_list.extend(temp)
            print part[0].upper()
            print 'cc_id %s' %(cc_id)
            print 'IF'
            pprint(if_list)
            print 'ID'
            pprint(id_list)
            print 'EX'
            pprint(ex_list)
            print 'WB'
            pprint(wb_list)
            print 'dest_list'
            pprint(dest_list)
            print 'RAW HAZARD'
            pprint(raw_hazard)
            print 'WAW HAZARD'
            pprint(waw_hazard)
            print 'STRUCT HAZARD'
            pprint(struct_hazard)
            cc_wb=''
            cc_ex=''
            raw_hazard[-1]='N'
            waw_hazard[-1]='N'
            struct_hazard[-1]='N'
            if len(fetch_inst)<5:
                fo. write('\n%s\t\t\t\t\t\t\t\t%s\t\t%s\t\t%s\t\t%s\t\t%s\t\tN\t\t%s\t\t%s' % (fetch_inst,cc_if,cc_id,cc_ex,cc_wb,raw_hazard[-1],waw_hazard[-1],struct_hazard[-1]))
            fo.write('\n\nTotal number of requests to instruction cache %s' % (ic_access))
            fo.write('\nTotal number of instruction cache hit %s' %(ic_hit))
            fo.write('\nTotal number of requests to data cache  %s' %(dc_access))
            fo.write('\nTotal number of data cache hit %s' %(dc_hit))

            break

    print 'cc_id is %s' % (cc_id)
    #print 'ID LIST'
    #pprint(id_list)
    print
    #print 'SOURCE LIST '
    #pprint(source_list)
    print

    #Execution Stage
    print 'Execution Stage'
    # perform the respective arithmetic or logical operations

    if opcode.strip().upper()=='LW':
        cc_ex=cc_id+1
        data_memory_ld=src_ld+int(offset)
        print 'data source + offset LW is %s' % (data_memory_ld)
        print 'destination is %s' % (dest)
        #print
    if opcode.strip().upper()=='SW':
        cc_ex=cc_id+1
        data_memory_st=dst_st+int(offset)
        print 'data dest + offset SW is %s' % (data_memory_st)
        print 'source is %s' % (source)
        #print
    if opcode.strip().upper()=='L.D':
        cc_ex=cc_id+1
        data_memory_ld=src_ld+int(offset)
        data_memory1_ld=data_memory_ld+4
        print 'data source + offset L.D is %s' % (data_memory_ld)
        print 'data mem1 L.D is %s' % (data_memory1_ld)
        print 'destination is %s' % (dest)
        #print
    if opcode.strip().upper()=='S.D':
        cc_ex=cc_id+1
        data_memory_st=dst_st+int(offset)
        data_memory1_st=data_memory_st+4
        #print 'data dest + offset S.D is %s' % (data_memory_st)
        #print 'source is %s' % (source)
        #print
    if opcode.strip().upper()=='DADD':
        cc_ex=cc_id+2
        for wb in wb_list:
            if ',' not in wb:
                clk=int(wb)
                if (clk==cc_ex+1):
                    cc_ex=clk+1
        temp=[]
        temp.append(fetch_inst)
        temp.append(str(cc_ex))
        ex_list.extend(temp)
        ex1_list.append(temp)
        dst=src1+src2
        #print 'destination value DADD is %s' % (dst)
        #print
    if opcode.strip().upper()=='DADDI':
        cc_ex=cc_id+2
        for wb in wb_list:
            if ',' not in wb:
                clk=int(wb)
                if (clk==cc_ex+1):
                    cc_ex=clk+1
        temp=[]
        temp.append(fetch_inst)
        temp.append(str(cc_ex))
        ex_list.extend(temp)
        ex1_list.append(temp)
        dst=src1+src2
        #print 'destination value DADDI is %s' % (dst)
        #print
        
    if opcode.strip().upper()=='DSUB':
        cc_ex=cc_id+2
        for wb in wb_list:
            if ',' not in wb:
                clk=int(wb)
                if (clk==cc_ex+1):
                    cc_ex=clk+1
        temp=[]
        temp.append(fetch_inst)
        temp.append(str(cc_ex))
        ex_list.extend(temp)
        ex1_list.append(temp)
        dst=src1-src2
        #print 'destination value DSUB is %s' % (dst)
        #print
    if opcode.strip().upper()=='DSUBI':
        cc_ex=cc_id+2
        for wb in wb_list:
            if ',' not in wb:
                clk=int(wb)
                if (clk==cc_ex+1):
                    cc_ex=clk+1
        temp=[]
        temp.append(fetch_inst)
        temp.append(str(cc_ex))
        ex_list.extend(temp)
        ex1_list.append(temp)
        dst=src1-src2
        #print 'destination value DSUBI is %s' % (dst)
        #print
    if opcode.strip().upper()=='AND':
        cc_ex=cc_id+2
        for wb in wb_list:
            if ',' not in wb:
                clk=int(wb)
                if (clk==cc_ex+1):
                    cc_ex=clk+1
        temp=[]
        temp.append(fetch_inst)
        temp.append(str(cc_ex))
        ex_list.extend(temp)
        ex1_list.append(temp)
        dst= (src1 & src2)
        #print 'destination value AND is %s' % (dst)
        #print
    if opcode.strip().upper()=='ANDI':
        cc_ex=cc_id+2
        for wb in wb_list:
            if ',' not in wb:
                clk=int(wb)
                if (clk==cc_ex+1):
                    cc_ex=clk+1
        temp=[]
        temp.append(fetch_inst)
        temp.append(str(cc_ex))
        ex_list.extend(temp)
        ex1_list.append(temp)
        dst= (src1 & src2)
        #print 'destination value ANDI is %s' % (dst)
        #print
    if opcode.strip().upper()=='OR':
        cc_ex=cc_id+2
        for wb in wb_list:
            if ',' not in wb:
                clk=int(wb)
                if (clk==cc_ex+1):
                    cc_ex=clk+1
        temp=[]
        temp.append(fetch_inst)
        temp.append(str(cc_ex))
        ex_list.extend(temp)
        ex1_list.append(temp)
        dst= (src1|src2)
        #print 'destination value OR is %s' % (dst)
        #print
    if opcode.strip().upper()=='ORI':
        cc_ex=cc_id+2
        for wb in wb_list:
            if ',' not in wb:
                clk=int(wb)
                if (clk==cc_ex+1):
                    cc_ex=clk+1
        temp=[]
        temp.append(fetch_inst)
        temp.append(str(cc_ex))
        ex_list.extend(temp)
        ex1_list.append(temp)
        dst= src1|src2
        #print 'destination value ORI is %s' % (dst)
        #print
    if opcode.strip().upper()=='ADD.D':
        config_typ=config['FP ADDER']
        config_value=config_typ.strip().split(',')
        config_time=int(config_value[0])
        pipelined=config_value[1]
        flag=False
        for ex in ex_list:
            if ',' in ex:
                part=ex.strip().split(',')
                partition=part[0].strip().split()
                if len(partition)>2:
                    op=partition[1].strip()
                else:
                    op=partition[0].strip()
                if op=='ADD.D' or op=='SUB.D':
                    inst_index=ex_list.index(ex)
                    clk=ex_list[inst_index+1]
                    if pipelined=='no':
                        if(clk>=cc_ex):
                            cc_ex=int(clk)+config_time
                            struct_hazard.pop()
                            struct_hazard.pop()
                            struct_hazard.append(fetch_inst)
                            struct_hazard.append('Y')
                            flag=True
                        else:
                            cc_ex=cc_id+config_time
                            flag=True
                    else:
                        cc_ex=cc_id+config_time
                        flag=True
            elif flag==False:
                cc_ex=cc_id+config_time

        for wb in wb_list:
            if ',' not in wb:
                clk=int(wb)
                if (clk==cc_ex+1):
                    cc_ex=clk+1
        temp=[]
        temp.append(fetch_inst)
        temp.append(str(cc_ex))
        ex_list.extend(temp)
        ex1_list.append(temp)
        
    if opcode.strip().upper()=='MUL.D':
        config_typ=config['FP MULTIPLIER']
        config_value=config_typ.strip().split(',')
        config_time=int(config_value[0])
        pipelined=config_value[1]
        flag=False
        for ex in ex_list:
            if ',' in ex:
                part=ex.strip().split(',')
                partition=part[0].strip().split()
                if len(partition)>2:
                    op=partition[1].strip()
                else:
                    op=partition[0].strip()
                if op=='MUL.D':
                    inst_index=ex_list.index(ex)
                    clk=ex_list[inst_index+1]
                    if pipelined=='no':
                        if(clk>=cc_ex):
                            cc_ex=int(clk)+config_time
                            struct_hazard.pop()
                            struct_hazard.pop()
                            struct_hazard.append(fetch_inst)
                            struct_hazard.append('Y')
                            flag=True
                        else:
                            cc_ex=cc_id+config_time
                            flag=True
                    else:
                        cc_ex=cc_id+config_time
                        flag=True
            elif flag==False:
                cc_ex=cc_id+config_time

        for wb in wb_list:
            if ',' not in wb:
                clk=int(wb)
                if (clk==cc_ex+1):
                    cc_ex=clk+1
        temp=[]
        temp.append(fetch_inst)
        temp.append(str(cc_ex))
        ex_list.extend(temp)
        ex1_list.append(temp)
        
    if opcode.strip().upper()=='DIV.D':
        config_typ=config['FP DIVIDER']
        config_value=config_typ.strip().split(',')
        config_time=int(config_value[0])
        pipelined=config_value[1]
        flag=False
        for ex in ex_list:
            if ',' in ex:
                part=ex.strip().split(',')
                partition=part[0].strip().split()
                if len(partition)>2:
                    op=partition[1].strip()
                else:
                    op=partition[0].strip()
                if op=='DIV.D':
                    inst_index=ex_list.index(ex)
                    clk=ex_list[inst_index+1]
                    if pipelined=='no':
                        if(clk>=cc_ex):
                            cc_ex=int(clk)+config_time
                            struct_hazard.pop()
                            struct_hazard.pop()
                            struct_hazard.append(fetch_inst)
                            struct_hazard.append('Y')
                            flag=True
                        else:
                            cc_ex=cc_id+config_time
                            flag=True
                    else:
                        cc_ex=cc_id+config_time
                        flag=True
            elif flag==False:
                cc_ex=cc_id+config_time

        for wb in wb_list:
            if ',' not in wb:
                clk=int(wb)
                if (clk==cc_ex+1):
                    cc_ex=clk+1
        temp=[]
        temp.append(fetch_inst)
        temp.append(str(cc_ex))
        ex_list.extend(temp)
        ex1_list.append(temp)
        
    if opcode.strip().upper()=='SUB.D':
        config_typ=config['FP ADDER']
        config_value=config_typ.strip().split(',')
        config_time=int(config_value[0])
        pipelined=config_value[1]
        flag=False
        for ex in ex_list:
            if ',' in ex:
                part=ex.strip().split(',')
                partition=part[0].strip().split()
                if len(partition)>2:
                    op=partition[1].strip()
                else:
                    op=partition[0].strip()
                if op=='ADD.D' or op=='SUB.D':
                    inst_index=ex_list.index(ex)
                    clk=ex_list[inst_index+1]
                    if pipelined=='no':
                        if(clk>=cc_ex):
                            cc_ex=int(clk)+config_time
                            struct_hazard.pop()
                            struct_hazard.pop()
                            struct_hazard.append(fetch_inst)
                            struct_hazard.append('Y')
                            flag=True
                        else:
                            cc_ex=cc_id+config_time
                            flag=True
                    else:
                        cc_ex=cc_id+config_time
                        flag=True
            elif flag==False:
                cc_ex=cc_id+config_time
        

        for wb in wb_list:
            if ',' not in wb:
                clk=int(wb)
                if (clk==cc_ex+1):
                    cc_ex=clk+1
        temp=[]
        temp.append(fetch_inst)
        temp.append(str(cc_ex))
        ex_list.extend(temp)
        ex1_list.append(temp)
        
    #print 'EX LIST'
    #pprint(ex1_list)
    print 'cc_ex is %s' %(cc_ex)
    if opcode=='LW' or opcode=='L.D' or opcode=='SW' or opcode=='S.D': 
        print "data cache"
        pprint (data_cache)

    #Data cache inplementation for Load
    if opcode.strip().upper()=='LW':
        T=int(config['MAIN MEMORY'])
        k=int(config['D-CACHE'])
        flag=False
        if data_cache==[[[],[]],[[],[]]]:
            cc_ex=cc_ex+(2*(T+k))
            dc_access+=1
            for l in data:
                if(l[1]==hex(data_memory_ld)):
                    blk_num=l[0]
            for i in data:
                if i[0]==blk_num:
                    data_index=i[0]%2
                    if data_index==0:
                        data_cache[data_index][0].append(i)
                    elif data_index==1:
                        data_cache[data_index][0].append(i)

            for blk in data_cache:
                for part in blk:
                    for ins in part:
                        if(ins[1]==hex(data_memory_ld)):
                            register[dest]=ins[2]
                            for ins in part:
                                ins[3]+=1
                            flag=True
        else:
            for blk in data_cache:
                for part in blk:
                    for ins in part:
                        if(ins[1]==hex(data_memory_ld)):
                            register[dest]=ins[2]
                            dc_access+=1
                            dc_hit+=1
                            for ins in part:
                                ins[3]+=1
                            flag=True
                            
                    #Check for Struct Hazard
                            for ex1 in ex1_list:
                                if ',' in ex1[0]:
                                    part=ex1[0].strip().split(',')
                                    partition=part[0].strip().split()
                                    if len(partition)>2:
                                        op=partition[1].strip()
                                    else:
                                        op=partition[0].strip()
                                    clk = int(ex1[1])
                                    if op=='LW' or op=='L.D' or op=='SW' or op=='S.D':
                                        if(clk > cc_ex or clk==cc_ex):
                                            cc_ex=clk+1
                                            struct_hazard.pop()
                                            struct_hazard.pop()
                                            struct_hazard.append(fetch_inst)
                                            struct_hazard.append('Y')
                            cc_ex+=1
                            
##                            for ex in ex_list:
##                                if ',' in ex:
##                                    part=ex.strip().split(',')
##                                    partition=part[0].strip().split()
##                                    if len(partition)>2:
##                                        op=partition[1].strip()
##                                    else:
##                                        op=partition[0].strip()
##                                    if op=='LW' or op=='L.D' or op=='SW' or op=='S.D':
##                                        inst_index=ex_list.index(ex)
##                                        clk=ex_list[inst_index+1]
##                                        if(int(clk)> cc_ex or int(clk)==cc_ex):
##                                            cc_ex=int(clk)+1
##                                            struct_hazard.pop()
##                                            struct_hazard.pop()
##                                            struct_hazard.append(fetch_inst)
##                                            struct_hazard.append('Y')
                            
                                               
            if flag==False:
                for l in data:
                    if(l[1]==hex(data_memory_ld)):
                        blk_num=l[0]
                for i in data:
                    if i[0]==blk_num:
                        data_index=i[0]%2
                        if data_index==0:
                            if len(data_cache[0][0])<4:
                                data_cache[0][0].append(i)
                            elif len(data_cache[0][1])<4:
                                data_cache[0][1].append(i)
                            else:
                                if data_cache[0][0][0][3]<data_cache[0][1][0][3]:
                                    for item in data_cache[0][0]:
                                        if item[3]>i[3]:
                                            if i[0]==blk_num:
                                                data_cache[0][0].append(i)
                                elif data_cache[0][0][0][3]>data_cache[0][1][0][3]:
                                    for item in data_cache[0][1]:
                                        if item[3]>i[3]:
                                            if i[0]==blk_num:
                                                data_cache[0][1].append(i)

                        if data_index==1:
                            if len(data_cache[1][0])<4:
                                data_cache[1][0].append(i)
                            elif len(data_cache[1][1])<4:
                                data_cache[1][1].append(i)
                            else:
                                if data_cache[1][0][0][3]<data_cache[1][1][0][3]:
                                    for item in data_cache[1][0]:
                                        if item[3]>i[3]:
                                            if i[0]==blk_num:
                                                data_cache[1][0].append(i)
                                    data_cache[1][0].append(i)
                                elif data_cache[1][0][0][3]>data_cache[1][1][0][3]:
                                    for item in data_cache[1][1]:
                                        if item[3]>i[3]:
                                            if i[0]==blk_num:
                                                data_cache[1][1].append(i)
                                    data_cache[1][1].append(i)
                           
                for blk in data_cache:
                    for part in blk:
                        for ins in part:
                            if(ins[1]==hex(data_memory_ld)):
                                register[dest]=ins[2]
                                dc_access+=1
                                for ins in part:
                                    ins[3]+=1
                                flag=True
                        #Check for Struct Hazard
                                for ex1 in ex1_list:
                                    if ',' in ex1[0]:
                                        part=ex1[0].strip().split(',')
                                        partition=part[0].strip().split()
                                        if len(partition)>2:
                                            op=partition[1].strip()
                                        else:
                                            op=partition[0].strip()
                                        clk = int(ex1[1])
                                        if op=='LW' or op=='L.D' or op=='SW' or op=='S.D':
                                            if(clk > cc_ex or clk==cc_ex):
                                                cc_ex=clk+1
                                                struct_hazard.pop()
                                                struct_hazard.pop()
                                                struct_hazard.append(fetch_inst)
                                                struct_hazard.append('Y') 

                                cc_ex=cc_ex+(2*(T+k))
##                                for ex in ex_list:
##                                    if ',' in ex:
##                                        part=ex.strip().split(',')
##                                        partition=part[0].strip().split()
##                                        if len(partition)>2:
##                                            op=partition[1].strip()
##                                        else:
##                                            op=partition[0].strip()
##                                        if op=='LW' or op=='L.D' or op=='SW' or op=='S.D':
##                                            inst_index=ex_list.index(ex)
##                                            clk=ex_list[inst_index+1]
##                                            if(int(clk)> cc_ex or int(clk)==cc_ex):
##                                                cc_ex=int(clk)+1
##                                                struct_hazard.pop()
##                                                struct_hazard.pop()
##                                                struct_hazard.append(fetch_inst)
##                                                struct_hazard.append('Y')
                                


    if opcode.strip().upper()=='L.D':

        T=int(config['MAIN MEMORY'])
        k=int(config['D-CACHE'])             
        flag=False
        if data_cache==[[[],[]],[[],[]]]:
            cc_ex=cc_ex+(2*(T+k))
            dc_access+=1
            for l in data:
                if(l[1]==hex(data_memory_ld)):
                    blk_num=l[0]
            for i in data:
                if i[0]==blk_num:
                    data_index=i[0]%2
                    if data_index==0:
                        data_cache[data_index][0].append(i)
                    elif data_index==1:
                        data_cache[data_index][0].append(i)

            for blk in data_cache:
                for part in blk:
                    for ins in part:
                        if(ins[1]==hex(data_memory_ld)):
                            for ins in part:
                                ins[3]+=1
                            flag=True
        else:
            for blk in data_cache:
                for part in blk:
                    for ins in part:
                        if(ins[1]==hex(data_memory_ld)):
                            
                            dc_access+=1
                            dc_hit+=1
                            for ins in part:
                                ins[3]+=1
                            flag=True
                            
                    #Check for Struct Hazard
                            for ex1 in ex1_list:
                                if ',' in ex1[0]:
                                    part=ex1[0].strip().split(',')
                                    partition=part[0].strip().split()
                                    if len(partition)>2:
                                        op=partition[1].strip()
                                    else:
                                        op=partition[0].strip()
                                    clk = int(ex1[1])
                                    if op=='LW' or op=='L.D' or op=='SW' or op=='S.D':
                                        if(clk > cc_ex or clk==cc_ex):
                                            cc_ex=clk+1
                                            struct_hazard.pop()
                                            struct_hazard.pop()
                                            struct_hazard.append(fetch_inst)
                                            struct_hazard.append('Y')
                            cc_ex+=1
##                            for ex in ex_list:
##                                if ',' in ex:
##                                    part=ex.strip().split(',')
##                                    partition=part[0].strip().split()
##                                    if len(partition)>2:
##                                        op=partition[1].strip()
##                                    else:
##                                        op=partition[0].strip()
##                                    if op=='LW' or op=='L.D' or op=='SW' or op=='S.D':
##                                        inst_index=ex_list.index(ex)
##                                        clk=ex_list[inst_index+1]
##                                        if(int(clk)> cc_ex or int(clk)==cc_ex):
##                                            cc_ex=int(clk)+1
##                                            struct_hazard.pop()
##                                            struct_hazard.pop()
##                                            struct_hazard.append(fetch_inst)
##                                            struct_hazard.append('Y')
                            
                                       
            if flag==False:
                for l in data:
                    if(l[1]==hex(data_memory_ld)):
                        print 'hello'
                        blk_num=l[0]
                        
                for i in data:
                    if i[0]==blk_num:
                        data_index=i[0]%2
                        if data_index==0:
                            if len(data_cache[0][0])<4:
                                data_cache[0][0].append(i)
                            elif len(data_cache[0][1])<4:
                                data_cache[0][1].append(i)
                            else:
                                if data_cache[0][0][0][3]<data_cache[0][1][0][3]:
                                    for item in data_cache[0][0]:
                                        if item[3]>i[3]:
                                            if i[0]==blk_num:
                                                data_cache[0][0].append(i)
                                elif data_cache[0][0][0][3]>data_cache[0][1][0][3]:
                                    for item in data_cache[0][1]:
                                        if item[3]>i[3]:
                                            if i[0]==blk_num:
                                                data_cache[0][1].append(i)
                        if data_index==1:
                            if len(data_cache[1][0])<4:
                                data_cache[1][0].append(i)
                            elif len(data_cache[1][1])<4:
                                data_cache[1][1].append(i)
                            else:
                                if data_cache[1][0][0][3]<data_cache[1][1][0][3]:
                                    for item in data_cache[1][0]:
                                        if item[3]>i[3]:
                                            if i[0]==blk_num:
                                                data_cache[1][0].append(i)
                                elif data_cache[1][0][0][3]>data_cache[1][1][0][3]:
                                    for item in data_cache[1][1]:
                                        if item[3]>i[3]:
                                            if i[0]==blk_num:
                                                data_cache[1][1].append(i)
                           
                for blk in data_cache:
                    for part in blk:
                        for ins in part:
                            if(ins[1]==hex(data_memory_ld)):
                                dc_access+=1
                                for ins in part:
                                    ins[3]+=1
                                flag=True
                        #Check for struct hazard
                                for ex1 in ex1_list:
                                    if ',' in ex1[0]:
                                        part=ex1[0].strip().split(',')
                                        partition=part[0].strip().split()
                                        if len(partition)>2:
                                            op=partition[1].strip()
                                        else:
                                            op=partition[0].strip()
                                        clk = int(ex1[1])
                                        if op=='LW' or op=='L.D' or op=='SW' or op=='S.D':
                                            if(clk> cc_ex or clk==cc_ex):
                                                cc_ex=clk+1
                                                struct_hazard.pop()
                                                struct_hazard.pop()
                                                struct_hazard.append(fetch_inst)
                                                struct_hazard.append('Y')
                                cc_ex=cc_ex+(2*(T+k))
##                                for ex in ex_list:
##                                    if ',' in ex:
##                                        part=ex.strip().split(',')
##                                        partition=part[0].strip().split()
##                                        if len(partition)>2:
##                                            op=partition[1].strip()
##                                        else:
##                                            op=partition[0].strip()
##                                        if op=='LW' or op=='L.D' or op=='SW' or op=='S.D':
##                                            inst_index=ex_list.index(ex)
##                                            clk=ex_list[inst_index+1]
##                                            if(int(clk)> cc_ex or int(clk)==cc_ex):
##                                                cc_ex=int(clk)+1
##                                                struct_hazard.pop()
##                                                struct_hazard.pop()
##                                                struct_hazard.append(fetch_inst)
##                                                struct_hazard.append('Y')

                                

        # load the second word of L.D
        flag=False
        for blk in data_cache:
                for part in blk:
                    for ins in part:
                        if(ins[1]==hex(data_memory1_ld)):
                            print 'yes1'
                            cc_ex+=1
                            dc_access+=1
                            dc_hit+=1
                            for ins in part:
                                ins[3]+=1
                            flag=True
        if flag==False:
            print 'yes2'
            for l in data:
                if(l[1]==hex(data_memory1_ld)):
                    blk_num=l[0]
                    cc_ex=cc_ex+(2*(T+k))
            for i in data:
                if i[0]==blk_num:
                    data_index=i[0]%2
                    if data_index==0:
                        if len(data_cache[0][0])<4:
                            data_cache[0][0].append(i)
                        elif len(data_cache[0][1])<4:
                            data_cache[0][1].append(i)
                        else:
                            if data_cache[0][0][0][3]<data_cache[0][1][0][3]:
                                for item in data_cache[0][0]:
                                    if item[3]>i[3]:
                                        if i[0]==blk_num:
                                            data_cache[0][0].append(i)
                            elif data_cache[0][0][0][3]>data_cache[0][1][0][3]:
                                for item in data_cache[0][1]:
                                    if item[3]>i[3]:
                                        if i[0]==blk_num:
                                            data_cache[0][1].append(i)
                    if data_index==1:
                        if len(data_cache[1][0])<4:
                            data_cache[1][0].append(i)
                        elif len(data_cache[1][1])<4:
                            data_cache[1][1].append(i)
                        else:
                            if data_cache[1][0][0][3]<data_cache[1][1][0][3]:
                                for item in data_cache[1][0]:
                                    if item[3]>i[3]:
                                        if i[0]==blk_num:
                                            data_cache[1][0].append(i)
                            elif data_cache[1][0][0][3]>data_cache[1][1][0][3]:
                                for item in data_cache[1][1]:
                                    if item[3]>i[3]:
                                        if i[0]==blk_num:
                                            data_cache[1][1].append(i)
                       
            for blk in data_cache:
                for part in blk:
                    for ins in part:
                        if(ins[1]==hex(data_memory1_ld)):
                            dc_access+=1
                            for ins in part:
                                ins[3]+=1
                            flag=True
                           
    if opcode.strip().upper()=='SW':
        T=int(config['MAIN MEMORY'])
        k=int(config['D-CACHE'])
        flag=False
        if data_cache==[[[],[]],[[],[]]]:
            cc_ex=cc_ex+(2*(T+k))
            dc_access+=1
            for l in data:
                if(l[1]==hex(data_memory_st)):
                    blk_num=l[0]
            for i in data:
                if i[0]==blk_num:
                    data_index=i[0]%2
                    if data_index==0:
                        data_cache[data_index][0].append(i)
                    elif data_index==1:
                        data_cache[data_index][0].append(i)

            for blk in data_cache:
                for part in blk:
                    for ins in part:
                        if(ins[1]==hex(data_memory_st)):
                            ins[2]=register[source]
                            ins[4]=1
                            for ins in part:
                                ins[3]+=1
                            flag=True
        else:
            for blk in data_cache:
                for part in blk:
                    for ins in part:
                        if(ins[1]==hex(data_memory_st)):
                            ins[2]=register[source]
                            dc_access+=1
                            dc_hit+=1
                            ins[4]=1
                            for ins in part:
                                ins[3]+=1
                            flag=True
                    #Check for struct hazard
                            for ex1 in ex1_list:
                                if ',' in ex1[0]:
                                    part=ex1[0].strip().split(',')
                                    partition=part[0].strip().split()
                                    if len(partition)>2:
                                        op=partition[1].strip()
                                    else:
                                        op=partition[0].strip()
                                    clk = int(ex1[1])
                                    if op=='LW' or op=='L.D' or op=='SW' or op=='S.D':
                                        if(clk> cc_ex or clk==cc_ex):
                                            cc_ex=clk+1
                                            struct_hazard.pop()
                                            struct_hazard.pop()
                                            struct_hazard.append(fetch_inst)
                                            struct_hazard.append('Y')
                            cc_ex+=1
##                            for ex in ex_list:
##                                if ',' in ex:
##                                    part=ex.strip().split(',')
##                                    partition=part[0].strip().split()
##                                    if len(partition)>2:
##                                        op=partition[1].strip()
##                                    else:
##                                        op=partition[0].strip()
##                                    if op=='LW' or op=='L.D' or op=='SW' or op=='S.D':
##                                        inst_index=ex_list.index(ex)
##                                        clk=ex_list[inst_index+1]
##                                        if(int(clk)> cc_ex or int(clk)==cc_ex):
##                                            cc_ex=int(clk)+1
##                                            struct_hazard.pop()
##                                            struct_hazard.pop()
##                                            struct_hazard.append(fetch_inst)
##                                            struct_hazard.append('Y')
                            
            if flag==False:
                for l in data:
                    if(l[1]==hex(data_memory_st)):
                        blk_num=l[0]
                        
                for i in data:
                    if i[0]==blk_num:
                        data_index=i[0]%2
                        if data_index==0:
                            if len(data_cache[0][0])<4:
                                data_cache[0][0].append(i)
                            elif len(data_cache[0][1])<4:
                                data_cache[0][1].append(i)
                            else:
                                if data_cache[0][0][0][3]<data_cache[0][1][0][3]:
                                    for ins in data_cache[0][0]:
                                       if ins[4]==1:
                                           addr=ins[1]
                                           for d in data:
                                               if(d[1]==addr):
                                                   d[2]=ins[2]
                                    for item in data_cache[0][0]:
                                        if item[3]>i[3]:
                                            if i[0]==blk_num:
                                                data_cache[0][0].append(i)
                                elif data_cache[0][0][0][3]>data_cache[0][1][0][3]:
                                    for ins in data_cache[0][1]:
                                       if ins[4]==1:
                                           addr=ins[1]
                                           for d in data:
                                               if(d[1]==addr):
                                                   d[2]=ins[2]
                                    for item in data_cache[0][1]:
                                        if item[3]>i[3]:
                                            if i[0]==blk_num:
                                                data_cache[0][1].append(i)
                        if data_index==1:
                            if len(data_cache[1][0])<4:
                                data_cache[1][0].append(i)
                            elif len(data_cache[1][1])<4:
                                data_cache[1][1].append(i)
                            else:
                                if data_cache[1][0][0][3]<data_cache[1][1][0][3]:
                                    for ins in data_cache[1][0]:
                                       if ins[4]==1:
                                           addr=ins[1]
                                           for d in data:
                                               if(d[1]==addr):
                                                   d[2]=ins[2]
                                    for item in data_cache[1][0]:
                                        if item[3]>i[3]:
                                            if i[0]==blk_num:
                                                data_cache[1][0].append(i)
                                elif data_cache[1][0][0][3]>data_cache[1][1][0][3]:
                                    for ins in data_cache[1][1]:
                                       if ins[4]==1:
                                           addr=ins[1]
                                           for d in data:
                                               if(d[1]==addr):
                                                   d[2]=ins[2]
                                    for item in data_cache[1][1]:
                                        if item[3]>i[3]:
                                            if i[0]==blk_num:
                                                data_cache[1][1].append(i)
                           
                for blk in data_cache:
                    for part in blk:
                        for ins in part:
                            if(ins[1]==hex(data_memory_st)):
                                ins[2]=register[source]
                                dc_access+=1
                                ins[4]=1
                                for ins in part:
                                    ins[3]+=1
                                flag=True
                        #Check for struct hazard
                                for ex1 in ex1_list:
                                    if ',' in ex1[0]:
                                        part=ex1[0].strip().split(',')
                                        partition=part[0].strip().split()
                                        if len(partition)>2:
                                            op=partition[1].strip()
                                        else:
                                            op=partition[0].strip()
                                        clk = int(ex1[1])
                                        if op=='LW' or op=='L.D' or op=='SW' or op=='S.D':
                                            if(clk> cc_ex or clk==cc_ex):
                                                cc_ex=clk+1
                                                struct_hazard.pop()
                                                struct_hazard.pop()
                                                struct_hazard.append(fetch_inst)
                                                struct_hazard.append('Y')

                                cc_ex=cc_ex+(2*(T+k))
##                                for ex in ex_list:
##                                    if ',' in ex:
##                                        part=ex.strip().split(',')
##                                        partition=part[0].strip().split()
##                                        if len(partition)>2:
##                                            op=partition[1].strip()
##                                        else:
##                                            op=partition[0].strip()
##                                        if op=='LW' or op=='L.D' or op=='SW' or op=='S.D':
##                                            inst_index=ex_list.index(ex)
##                                            clk=ex_list[inst_index+1]
##                                            if(int(clk)> cc_ex or int(clk)==cc_ex):
##                                                cc_ex=int(clk)+1
##                                                struct_hazard.pop()
##                                                struct_hazard.pop()
##                                                struct_hazard.append(fetch_inst)
##                                                struct_hazard.append('Y')
                                

    if opcode.strip().upper()=='S.D':
        T=int(config['MAIN MEMORY'])
        k=int(config['D-CACHE'])
        flag=False
        if data_cache==[[[],[]],[[],[]]]:
            print 'hi'
            cc_ex=cc_ex+(2*(T+k))+1
            dc_access+=1
            for l in data:
                if(l[1]==hex(data_memory_st)):
                    blk_num=l[0]
            for i in data:
                if i[0]==blk_num:
                    data_index=i[0]%2
                    if data_index==0:
                        data_cache[data_index][0].append(i)
                    elif data_index==1:
                        data_cache[data_index][0].append(i)

            for blk in data_cache:
                for part in blk:
                    for ins in part:
                        if(ins[1]==hex(data_memory_st)):
                            for ins in part:
                                ins[3]+=1
                            flag=True
        else:
            print 'hello'
            for blk in data_cache:
                for part in blk:
                    for ins in part:
                        if(ins[1]==hex(data_memory_st)):
                            print 'yes'
                            dc_access+=1
                            dc_hit+=1
                            for ins in part:
                                ins[3]+=1
                            flag=True
                        #Check for struct hazard
                            for ex1 in ex1_list:
                                if ',' in ex1[0]:
                                    part=ex1[0].strip().split(',')
                                    partition=part[0].strip().split()
                                    if len(partition)>2:
                                        op=partition[1].strip()
                                    else:
                                        op=partition[0].strip()
                                    clk = int(ex1[1])
                                    if op=='LW' or op=='L.D' or op=='SW' or op=='S.D':
                                        if(clk> cc_ex or clk==cc_ex):
                                            cc_ex=clk+1
                                            struct_hazard.pop()
                                            struct_hazard.pop()
                                            struct_hazard.append(fetch_inst)
                                            struct_hazard.append('Y')
                            cc_ex+=1
##                            for ex in ex_list:
##                                if ',' in ex:
##                                    part=ex.strip().split(',')
##                                    partition=part[0].strip().split()
##                                    if len(partition)>2:
##                                        op=partition[1].strip()
##                                    else:
##                                        op=partition[0].strip()
##                                    if op=='LW' or op=='L.D' or op=='SW' or op=='S.D':
##                                        inst_index=ex_list.index(ex)
##                                        clk=ex_list[inst_index+1]
##                                        if(int(clk)> cc_ex or int(clk)==cc_ex):
##                                            cc_ex=int(clk)+1
##                                            struct_hazard.pop()
##                                            struct_hazard.pop()
##                                            struct_hazard.append(fetch_inst)
##                                            struct_hazard.append('Y')
                            
                            
            if flag==False:
                for l in data:
                    if(l[1]==hex(data_memory_st)):
                        blk_num=l[0]
                        
                for i in data:
                    if i[0]==blk_num:
                        data_index=i[0]%2
                        if data_index==0:
                            if len(data_cache[0][0])<4:
                                data_cache[0][0].append(i)
                            elif len(data_cache[0][1])<4:
                                data_cache[0][1].append(i)
                            else:
                                if data_cache[0][0][0][3]<data_cache[0][1][0][3]:
                                    for item in data_cache[0][0]:
                                        if item[3]>i[3]:
                                            if i[0]==blk_num:
                                                data_cache[0][0].append(i)
                                elif data_cache[0][0][0][3]>data_cache[0][1][0][3]:
                                    for item in data_cache[0][1]:
                                        if item[3]>i[3]:
                                            if i[0]==blk_num:
                                                data_cache[0][1].append(i)
                        if data_index==1:
                            if len(data_cache[1][0])<4:
                                data_cache[1][0].append(i)
                            elif len(data_cache[1][1])<4:
                                data_cache[1][1].append(i)
                            else:
                                if data_cache[1][0][0][3]<data_cache[1][1][0][3]:
                                    for item in data_cache[1][0]:
                                        if item[3]>i[3]:
                                            if i[0]==blk_num:
                                                data_cache[1][0].append(i)
                                elif data_cache[1][0][0][3]>data_cache[1][1][0][3]:
                                    for item in data_cache[1][1]:
                                        if item[3]>i[3]:
                                            if i[0]==blk_num:
                                                data_cache[1][1].append(i)
                           
                for blk in data_cache:
                    for part in blk:
                        for ins in part:
                            if(ins[1]==hex(data_memory_st)):
                                dc_access+=1
                                for ins in part:
                                    ins[3]+=1
                                flag=True
                            #Check for struct hazard
                                for ex1 in ex1_list:
                                    if ',' in ex1[0]:
                                        part=ex1[0].strip().split(',')
                                        partition=part[0].strip().split()
                                        if len(partition)>2:
                                            op=partition[1].strip()
                                        else:
                                            op=partition[0].strip()
                                        clk = int(ex1[1])
                                        if op=='LW' or op=='L.D' or op=='SW' or op=='S.D':
                                            if(clk> cc_ex or clk==cc_ex):
                                                cc_ex=clk+1
                                                struct_hazard.pop()
                                                struct_hazard.pop()
                                                struct_hazard.append(fetch_inst)
                                                struct_hazard.append('Y')
                                cc_ex=cc_ex+(2*(T+k))
##                                for ex in ex_list:
##                                    if ',' in ex:
##                                        part=ex.strip().split(',')
##                                        partition=part[0].strip().split()
##                                        if len(partition)>2:
##                                            op=partition[1].strip()
##                                        else:
##                                            op=partition[0].strip()
##                                        if op=='LW' or op=='L.D' or op=='SW' or op=='S.D':
##                                            inst_index=ex_list.index(ex)
##                                            clk=ex_list[inst_index+1]
##                                            if(int(clk)> cc_ex or int(clk)==cc_ex):
##                                                cc_ex=int(clk)+1
##                                                struct_hazard.pop()
##                                                struct_hazard.pop()
##                                                struct_hazard.append(fetch_inst)
##                                                struct_hazard.append('Y')

                                
        # Store second word of S.D
        flag=False
        for blk in data_cache:
            for part in blk:
                for ins in part:
                    if(ins[1]==hex(data_memory1_st)):
                        cc_ex+=1
                        dc_access+=1
                        dc_hit+=1
                        for ins in part:
                            ins[3]+=1
                        flag=True
        if flag==False:
            for l in data:
                if(l[1]==hex(data_memory1_st)):
                    blk_num=l[0]
                    cc_ex=cc_ex+(2*(T+k))
            for i in data:
                if i[0]==blk_num:
                    data_index=i[0]%2
                    if data_index==0:
                        if len(data_cache[0][0])<4:
                            data_cache[0][0].append(i)
                        elif len(data_cache[0][1])<4:
                            data_cache[0][1].append(i)
                        else:
                            if data_cache[0][0][0][3]<data_cache[0][1][0][3]:
                                for item in data_cache[0][0]:
                                    if item[3]>i[3]:
                                        if i[0]==blk_num:
                                            data_cache[0][0].append(i)
                            elif data_cache[0][0][0][3]>data_cache[0][1][0][3]:
                                for item in data_cache[0][1]:
                                    if item[3]>i[3]:
                                        if i[0]==blk_num:
                                            data_cache[0][1].append(i)
                    if data_index==1:
                        if len(data_cache[1][0])<4:
                            data_cache[1][0].append(i)
                        elif len(data_cache[1][1])<4:
                            data_cache[1][1].append(i)
                        else:
                            if data_cache[1][0][0][3]<data_cache[1][1][0][3]:
                                for item in data_cache[1][0]:
                                    if item[3]>i[3]:
                                        if i[0]==blk_num:
                                            data_cache[1][0].append(i)
                            elif data_cache[1][0][0][3]>data_cache[1][1][0][3]:
                                for item in data_cache[1][1]:
                                    if item[3]>i[3]:
                                        if i[0]==blk_num:
                                            data_cache[1][1].append(i)
 
            for blk in data_cache:
                for part in blk:
                    for ins in part:
                        if(ins[1]==hex(data_memory1_st)):
                            dc_access+=1
                            for ins in part:
                                ins[3]+=1
                            flag=True

    if opcode=='LW' or opcode=='L.D' or opcode=='SW' or opcode=='S.D': 
        print "data cache"
        pprint (data_cache)
    print cc_ex
    if opcode.strip().upper()=='LW':
        for wb in wb_list:
            if ',' not in wb:
                clk=int(wb)
                if (clk==cc_ex+1):
                    cc_ex=clk+1
        temp=[]
        temp.append(fetch_inst)
        temp.append(str(cc_ex))
        ex_list.extend(temp)
        ex1_list.append(temp)
        
    if opcode.strip().upper()=='SW':
        for wb in wb_list:
            if ',' not in wb:
                clk=int(wb)
                if (clk==cc_ex+1):
                    cc_ex=clk+1
        temp=[]
        temp.append(fetch_inst)
        temp.append(str(cc_ex))
        ex_list.extend(temp)
        ex1_list.append(temp)
        
    if opcode.strip().upper()=='L.D':
        for wb in wb_list:
            if ',' not in wb:
                clk=int(wb)
                if (clk==cc_ex+1):
                    cc_ex=clk+1
        temp=[]
        temp.append(fetch_inst)
        temp.append(str(cc_ex))
        ex_list.extend(temp)
        ex1_list.append(temp)
        
    if opcode.strip().upper()=='S.D':
        for wb in wb_list:
            if ',' not in wb:
                clk=int(wb)
                if (clk==cc_ex+1):
                    cc_ex=clk+1
        temp=[]
        temp.append(fetch_inst)
        temp.append(str(cc_ex))
        ex_list.extend(temp)
        ex1_list.append(temp)
        
    print 
    #Write Back Stage
    #print 'cc_ex is %s' %(cc_ex)
    #pprint(ex_list)
    
    if opcode.strip().upper()=='LW':
        cc_wb=cc_ex+1
        temp=[]
        temp.append(fetch_inst)
        temp.append(str(cc_wb))
        wb_list.extend(temp)

        temp1=[]
        temp1.append(dest)
        temp1.append(cc_wb)
        dest_list.extend(temp1)
        dst_list.append(temp1)

    if opcode.strip().upper()=='SW':
        cc_wb=cc_ex+1
        temp=[]
        temp.append(fetch_inst)
        temp.append(str(cc_wb))
        wb_list.extend(temp)

        temp1=[]
        temp1.append(dest)
        temp1.append(cc_wb)
        dest_list.extend(temp1)
        dst_list.append(temp1)

    if opcode.strip().upper()=='L.D':
        cc_wb=cc_ex+1
        temp=[]
        temp.append(fetch_inst)
        temp.append(str(cc_wb))
        wb_list.extend(temp)

        temp1=[]
        temp1.append(dest)
        temp1.append(cc_wb)
        dest_list.extend(temp1)
        dst_list.append(temp1)
        
    if opcode.strip().upper()=='S.D':
        cc_wb=cc_ex+1
        temp=[]
        temp.append(fetch_inst)
        temp.append(str(cc_wb))
        wb_list.extend(temp)

        temp1=[]
        temp1.append(dest)
        temp1.append(cc_wb)
        dest_list.extend(temp1)
        dst_list.append(temp1)
        
    if opcode.strip().upper()=='DADD':
        cc_wb=cc_ex+1
        temp=[]
        temp.append(fetch_inst)
        temp.append(str(cc_wb))
        wb_list.extend(temp)

        temp1=[]
        temp1.append(dest)
        temp1.append(cc_wb)
        dest_list.extend(temp1)
        dst_list.append(temp1)
        for key, value in register.items():
            if key==dest:
                register[key]=bin(dst)
                print 'dadd wb %s=%s' % (dest,register[key])
        
    if opcode.strip().upper()=='DADDI':
        cc_wb=cc_ex+1
        temp=[]
        temp.append(fetch_inst)
        temp.append(str(cc_wb))
        wb_list.extend(temp)

        temp1=[]
        temp1.append(dest)
        temp1.append(cc_wb)
        dest_list.extend(temp1)
        dst_list.append(temp1)
        for key, value in register.items():
            if key==dest:
                register[key]=bin(dst)
                print 'dadd wb %s=%s' % (dest,register[key])
    if opcode.strip().upper()=='DSUB':
        cc_wb=cc_ex+1
        temp=[]
        temp.append(fetch_inst)
        temp.append(str(cc_wb))
        wb_list.extend(temp)

        temp1=[]
        temp1.append(dest)
        temp1.append(cc_wb)
        dest_list.extend(temp1)
        dst_list.append(temp1)
        for key, value in register.items():
            if key==dest:
                register[key]=bin(dst)
                print 'dadd wb %s=%s' % (dest,register[key])
    if opcode.strip().upper()=='DSUBI':
        cc_wb=cc_ex+1
        temp=[]
        temp.append(fetch_inst)
        temp.append(str(cc_wb))
        wb_list.extend(temp)

        temp1=[]
        temp1.append(dest)
        temp1.append(cc_wb)
        dest_list.extend(temp1)
        dst_list.append(temp1)
        for key, value in register.items():
            if key==dest:
                register[key]=bin(dst)
                print 'dadd wb %s=%s' % (dest,register[key])
    if opcode.strip().upper()=='AND':
        cc_wb=cc_ex+1
        temp=[]
        temp.append(fetch_inst)
        temp.append(str(cc_wb))
        wb_list.extend(temp)

        temp1=[]
        temp1.append(dest)
        temp1.append(cc_wb)
        dest_list.extend(temp1)
        dst_list.append(temp1)
        for key, value in register.items():
            if key==dest:
                register[key]=bin(dst)
                print 'dadd wb %s=%s' % (dest,register[key])
    if opcode.strip().upper()=='ANDI':
        cc_wb=cc_ex+1
        temp=[]
        temp.append(fetch_inst)
        temp.append(str(cc_wb))
        wb_list.extend(temp)

        temp1=[]
        temp1.append(dest)
        temp1.append(cc_wb)
        dest_list.append(temp1)
        dst_list.append(temp1)
        for key, value in register.items():
            if key==dest:
                register[key]=bin(dst)
                print 'dadd wb %s=%s' % (dest,register[key])
    if opcode.strip().upper()=='OR':
        cc_wb=cc_ex+1
        temp=[]
        temp.append(fetch_inst)
        temp.append(str(cc_wb))
        wb_list.extend(temp)

        temp1=[]
        temp1.append(dest)
        temp1.append(cc_wb)
        dest_list.extend(temp1)
        dst_list.append(temp1)
        for key, value in register.items():
            if key==dest:
                register[key]=bin(dst)
                print 'dadd wb %s=%s' % (dest,register[key])
    if opcode.strip().upper()=='ORI':
        cc_wb=cc_ex+1
        temp=[]
        temp.append(fetch_inst)
        temp.append(str(cc_wb))
        wb_list.extend(temp)

        temp1=[]
        temp1.append(dest)
        temp1.append(cc_wb)
        dest_list.extend(temp1)
        dst_list.append(temp1)
        for key, value in register.items():
            if key==dest:
                register[key]=bin(dst)
                print 'dadd wb %s=%s' % (dest,register[key])
    if opcode.strip().upper()=='ADD.D':
        cc_wb=cc_ex+1
        temp=[]
        temp.append(fetch_inst)
        temp.append(str(cc_wb))
        wb_list.extend(temp)

        temp1=[]
        temp1.append(dest)
        temp1.append(cc_wb)
        dest_list.extend(temp1)
        dst_list.append(temp1)
        
    if opcode.strip().upper()=='MUL.D':
        cc_wb=cc_ex+1
        temp=[]
        temp.append(fetch_inst)
        temp.append(str(cc_wb))
        wb_list.extend(temp)

        temp1=[]
        temp1.append(dest)
        temp1.append(cc_wb)
        dest_list.extend(temp1)
        dst_list.append(temp1)
        
    if opcode.strip().upper()=='DIV.D':
        cc_wb=cc_ex+1
        temp=[]
        temp.append(fetch_inst)
        temp.append(str(cc_wb))
        wb_list.extend(temp)

        temp1=[]
        temp1.append(dest)
        temp1.append(cc_wb)
        dest_list.extend(temp1)
        dst_list.append(temp1)
        
    if opcode.strip().upper()=='SUB.D':
        cc_wb=cc_ex+1
        temp=[]
        temp.append(fetch_inst)
        temp.append(str(cc_wb))
        wb_list.extend(temp)

        temp1=[]
        temp1.append(dest)
        temp1.append(cc_wb)
        dest_list.extend(temp1)
        dst_list.append(temp1)
        
    print 'WRITE BACK STAGE'
    print 'cc_wb is %s' % (cc_wb)


    if len(fetch_inst)<16:
        fo. write('\n%s\t\t\t\t\t%s\t\t%s\t\t%s\t\t%s\t\t%s\t\tN\t\t%s\t\t%s' % (fetch_inst,cc_if,cc_id,cc_ex,cc_wb,raw_hazard[-1],waw_hazard[-1],struct_hazard[-1]))
    else:
        fo. write('\n%s\t\t\t\t%s\t\t%s\t\t%s\t\t%s\t\t%s\t\tN\t\t%s\t\t%s' % (fetch_inst,cc_if,cc_id,cc_ex,cc_wb,raw_hazard[-1],waw_hazard[-1],struct_hazard[-1]))
    
    
    
    
