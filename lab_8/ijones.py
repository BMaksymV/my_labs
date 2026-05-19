def solve():
    
    with open('ijones.in', 'r') as f_in:
        input_data = f_in.read().split()
        
    if not input_data:
        return
        
    W = int(input_data[0])
    H = int(input_data[1])
    grid = input_data[2 : 2+H]
    
    SumL = {chr(c): 0 for c in range(97, 123)} 
    P = [0] * H
    
    for x in range(H):
        P[x] = 1 
        char_c = grid[x][0]
        SumL[char_c] += 1
        
    for y in range(1, W):
        new_P = [0] * H
         
        for x in range(H):
            char_c = grid[x][y]
            paths = SumL[char_c]
            
            if grid[x][y-1] != char_c:
                paths += P[x]
                
            new_P[x] = paths
            
        for x in range(H):
            char_c = grid[x][y]
            SumL[char_c] += new_P[x]
            
        P = new_P
        
    if H == 1:
        ans = P[0]
    else:
        ans = P[0] + P[H-1]
        
    with open('ijones.out', 'w') as f_out:
        f_out.write(str(ans) + '\n')

if __name__ == '__main__':
    solve()