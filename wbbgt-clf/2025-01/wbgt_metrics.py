
def f1_score_loose(confusionMatrix):
    classCount = len(confusionMatrix[0])
    
    row = confusionMatrix[classIndex] 

def precision(confusionMatrix, classIndex):    
    column = [confusionMatrix[0][classIndex],
              confusionMatrix[1][classIndex],
              confusionMatrix[2][classIndex],
              confusionMatrix[3][classIndex]]
    print("Column", column)

    tpList = column[:classIndex+1]
    tp = sum(tpList)
    print("TP", tpList, tp)
    
    fpList = column[classIndex+1:]
    fp = sum(fpList)
    print("FP", fpList, fp)
    
    precision = tp/(tp+fp)
    print(precision)
    
    
    
#     for classIndex in classCount:
        
        

if __name__ == "__main__":
    confusionMatrix = [[148,   9,   0,   0],
                       [ 14, 129,  21,   0],
                       [  0,  18, 137,   8],
                       [  0,   4,  28, 136]]
#     f1_score_loose(confusionMatrix)
    for i in range(0,4):
        precision(confusionMatrix, i)
    
