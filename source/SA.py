import random
import math

def SA(mat, init_path, init_temp, cooling_rate, num_iter):
    # 計算距離
    def count_dist(mat, path):
        total_dist = 0        
        for i in range(len(path) - 1):
            total_dist += mat[path[i]][path[i + 1]]
        return total_dist
    # 初始解
    current_path = init_path
    current_dist = count_dist(mat, current_path)
    # 宣告最佳解
    best_path = []
    best_dist = float('inf')

    # 模擬退火法
    current_temp = init_temp

    for iter in range(num_iter):
        # 隨機對調兩個城市
        i, j = random.sample(range(1, len(mat)), 2)        
        new_path = current_path.copy()
        new_path[i], new_path[j] = new_path[j], new_path[i]
        # 計算新的總距離
        new_dist = count_dist(mat, new_path)
        
        # 如果出現更好解或是依據目前溫度、總距離差
        if new_dist < current_dist or random.random() < math.exp((current_dist - new_dist) / current_temp):
            current_path = new_path
            current_dist = new_dist
            # 更新最佳解
            if current_dist < best_dist:
                best_dist = current_dist
                best_path = current_path                
        
        current_temp *= cooling_rate
        print("iter:",iter,"current_temp:",current_temp," best_dist:", best_dist,"best_path:",best_path)
    return best_path, best_dist

if __name__ == "__main__":    
    mat = [
    # A   B   C   D   E
    [ 0,  1,  9,  8, 40], # A
    [ 1,  0,  2, 35, 50], # B
    [ 9,  2,  0, 30, 10], # C
    [ 8, 35, 30,  0,  5], # D
    [40, 50, 10,  5,  0]  # E
    ]

    init_path = [0, 1, 2, 3, 4, 0]
    init_temp = 1000
    cooling_rate = 0.99
    num_iter = 1000

    best_path, best_dist= SA(mat, init_path, init_temp, cooling_rate, num_iter)    
    
    print("最短路徑：", best_path)
    print("最短距離：", best_dist)    