import numpy as np

question = [[1,0,1,0,1,0,1,0],
            [2,1,2,1,2,1,2,1],
            [1,2,0,1,2,0,1,2],
            [1,0,1,0,1,0,1,0],
            [0,1,0,1,0,1,0,1],
            [2,0,1,2,0,1,2,0],
            [1,2,0,1,2,0,1,2],
            [0,1,2,0,1,2,0,1]]

qes = np.array(question)

for dx,dy in zip((0,2,2),(2,0,2)):
    GLCM = np.zeros([3,3], dtype = np.uint8)

    for i in range(8-dx):
        for j in range(8-dy):
            GLCM[qes[i][j]][qes[i+dx][j+dy]] += 1
    
    print(f"1/{np.sum(GLCM)}*\n", GLCM, '\n')


