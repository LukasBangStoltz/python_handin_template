import numpy as np
import matplotlib.pyplot as plt

filename = "../data/befkbhalderstatkode.csv"

bef_stats_df = np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)



neighb = {1: 'Indre By', 2: 'Østerbro', 3: 'Nørrebro', 4: 'Vesterbro/Kgs. Enghave', 
       5: 'Valby', 6: 'Vanløse', 7: 'Brønshøj-Husum', 8: 'Bispebjerg', 9: 'Amager Øst', 
       10: 'Amager Vest', 99: 'Udenfor'}


newDict = {}

def getPubInArea():
    for element in neighb:
        mask = (bef_stats_df[:,1] == element) & (bef_stats_df[:,0] == 2015)
        sum = np.sum(bef_stats_df[mask][:,4])
        print(neighb.get(element))
        print(sum)
        newDict.update({element: sum})


def plotCitys():
    sortedDict = {k: v for k, v in sorted(newDict.items(), key=lambda item: item[1])}
    for element in sortedDict:
        plt.bar([neighb.get(element)],[sortedDict.get(element)],width=0.5, align='center')
        plt.xticks(rotation=45, horizontalalignment='right',fontweight='light')

def findOldPeople():  
    mask = (bef_stats_df[:,0] == 2015) & (bef_stats_df[:,2] >65) & (bef_stats_df[:,1]!=99)
    sum = np.sum(bef_stats_df[mask][:,4])
    print("People above 65 in cph areas: " , sum)