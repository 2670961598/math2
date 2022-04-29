import xlrd
import networkx as nx
import matplotlib.pyplot as plt

def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

Dfile = xlrd.open_workbook('附件1.xlsx')
DInfo = Dfile.sheet_by_name('位置')
Einfo = Dfile.sheet_by_name('连线数据')
Rinfo = Dfile.sheet_by_name('任务')

print("共有" + str(DInfo.nrows - 1) + "节点") # 行数
print("共有" + str(Einfo.nrows - 1) + "个边") # 行数
G = nx.Graph()


placeList = []

for i in range(1 , DInfo.nrows):
    G.add_node((DInfo.cell(i,0).value,DInfo.cell(i,1).value,DInfo.cell(i,2).value))
    placeList.append((DInfo.cell(i,0).value,DInfo.cell(i,1).value,DInfo.cell(i,2).value))

for i in range(1 , Einfo.nrows):
    G.add_edge(placeList[int(Einfo.cell(i,1).value) - 1],placeList[int(Einfo.cell(i,2).value) - 1] , weight = distance(placeList[int(Einfo.cell(i,1).value) - 1][1],placeList[int(Einfo.cell(i,1).value) - 1][2],placeList[int(Einfo.cell(i,2).value) - 1][1],placeList[int(Einfo.cell(i,2).value) - 1][2]))
    # print(Einfo.cell(i,1).value,Einfo.cell(i,2).value)
    # print(G)
    print(distance(placeList[int(Einfo.cell(i,1).value) - 1][1],placeList[int(Einfo.cell(i,1).value) - 1][2],placeList[int(Einfo.cell(i,2).value) - 1][1],placeList[int(Einfo.cell(i,2).value) - 1][2]))
# print(G.nodes())
# print(G.edges())

nx.draw_networkx(G)
print(nx.dijkstra_path(G, source = placeList[0], target = placeList[100]))
print(nx.dijkstra_path_length(G, target = placeList[0], source = placeList[100]))
# print(nx.all_pairs_dijkstra_path(G)[placeList[0]])

Task = [0]*200
print(Task)
for i in range(1 , Rinfo.nrows):
    if int(Rinfo.cell(i , 2).value) == 1:
        print(int(Rinfo.cell(i , 1).value))
        Task[int(Rinfo.cell(i , 1).value) - 1] += 1
    else:
        break

mid = {}
print(Task)
for i in range(len(Task)):
    if Task[i] != 0:
        mid[i] = Task[i]
print(mid)

list = []
placeXY = []
for i in range(len(mid)):
    midList = []
    for j in range(len(mid)):
        if i == j:
            midList.append(0)
        else:
            midList.append(nx.dijkstra_path_length(G, target = placeList[i], source = placeList[j]))
    list.append(midList)

print(list)
print(placeXY)

for i in mid:
    a = placeList[i-1][1:]
    placeXY.append(a)
print(placeXY)
















