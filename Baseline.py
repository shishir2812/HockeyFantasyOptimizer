import pandas as pd
df=pd.read_csv("DataTable.csv")
pos_dict={"C":[],"W":[],"D":[],"G":[]}

for index, item in df.iterrows():
    # item=dict(item)
    # print(type(item))
    # print( item["DKPos"])
    if item["DKPos"] in pos_dict:
        pos_dict[item["DKPos"]].append({"DKSalary":item["DKSalary"],"FDFP":item["FDFP"],"PlayerID":item["PlayerID"]})

# print(pos_dict["G"])

#According to FDFP descending order, then according to DKSalary ascending order
for pos,item in  pos_dict.items():
    pos_dict[pos]=sorted(item, key=lambda x: (x["FDFP"],-float(x["DKSalary"])), reverse=True)

# print(pos_dict["G"])


budget=50000
#2G 3C 3W 2D
num_dict={"G":2,"C":3,"W":3,"D":2}
i=0
def get_player(i):
    while True:
        cost=0

        result_dict={"G":[],"C":[],"W":[],"D":[]}
        for pos in ["G","C","W","D"]:
            item=pos_dict[pos]
            #The greedy method is mainly used here, based on the sorted "G", "C", "W", "D". To be done. Because it is found that the salary of G C is relatively large, we give priority to them, and WD will directly take the largest salary. If not, then take the salary with the smaller G C
            if pos=="G":
                item=item[i:]
            if pos=="C":
                item=item[i:]
                # print(item[0])
            for value in item:
                if len(result_dict[pos])<num_dict[pos] and cost<=budget:
                    result_dict[pos].append(value)
                    cost+=value["DKSalary"]
                if len(result_dict["D"])==num_dict["D"] and len(result_dict["G"])==num_dict["G"] \
                and len(result_dict["W"])==num_dict["W"] and len(result_dict["C"])==num_dict["C"] :return result_dict,cost

        if len(result_dict["D"])==num_dict["D"] and len(result_dict["G"])==num_dict["G"] \
                and len(result_dict["W"])==num_dict["W"] and len(result_dict["C"])==num_dict["C"] :return result_dict,cost
        # print(result_dict)
        i+=1
        print(i)

result_dict,cost=get_player(i)
print(result_dict)
print(cost)