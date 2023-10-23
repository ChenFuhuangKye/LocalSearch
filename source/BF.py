def BF(mat):
    # 所有城市排列的組合
    def permutations(iterable):
        # 初始化參數
        pool = tuple(iterable)                                      # 將iterable轉成不可變的tuple
        n = len(pool)                                               # pool個數
        r = n                                                       # 目前排列的個數

        indices = list(range(n))                                    # 初始化排列，從 0 到 n-1
        cycles = list(range(n, n-r, -1))                            # 追蹤每個元素的出現次數, 從 n 到 n-r 的遞減
        yield tuple(pool[i] for i in indices[:r])                   # 生成目前排列        
        while n: # 生成所有組合直到所有排列生成完畢
            for i in reversed(range(r)):                            # 從最後一個元素向前尋找，每次减少cycles中的值。
                cycles[i] -= 1                                      # 如果cycles[i]等於0，代表這個元素的所有可能位置已经尋找完，需要重新排列。
                if cycles[i] == 0:
                    indices[i:] = indices[i+1:] + indices[i:i+1]
                    cycles[i] = n - i
                else:
                    j = cycles[i]
                    indices[i], indices[-j] = indices[-j], indices[i]    # 重新排列indices中的元素，以生成下一個排列。
                    yield tuple(pool[i] for i in indices[:r])            # 生成新的排列
                    break
            else:
                return
    
    # 參數宣告
    city_count = len(mat)     # 計算城市數量
    best_path = []            # 初始化最佳路徑
    best_dist = float('inf')  # 初始化最佳解

    # 找尋所有可能的組合
    for i in permutations([i for i in range(1, city_count)]):
        # 創建目前路徑，從0號城市開始，最後再回到0號城市
        path = [0]
        for city in i:            
            path.append(city)
        path.append(0)

        # 計算目前路徑的總距離
        total_dist = 0
        for i in range(len(path) - 1):
            total_dist += mat[path[i]][path[i + 1]]
        
        # 更改最佳解
        if total_dist < best_dist:
            best_dist = total_dist
            best_path = path
        print("path:", path, "best_path:",best_path, "best_dist:", best_dist )
    return best_path, best_dist

if __name__ == "__main__":    
    # 距離矩陣
    mat = [
    # A   B   C   D   E
    [ 0,  1,  9,  8, 40], # A
    [ 1,  0,  2, 35, 50], # B
    [ 9,  2,  0, 30, 10], # C
    [ 8, 35, 30,  0,  5], # D
    [40, 50, 10,  5,  0]  # E
    ]

    best_path, best_dist = BF(mat)    
    
    print("最短路徑：", best_path)
    print("最短距離：", best_dist)    