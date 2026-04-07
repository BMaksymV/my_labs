from collections import deque

def flood_fill(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"No file found")
        return

    height, width = map(int, lines[0].split(','))
    start_r, start_c = map(int, lines[1].split(','))
    replacement_color = lines[2].replace('‘', '').replace('’', '').replace("'", "").replace('"', '')

    grid = []
    for line in lines[3:]:
        clean_line = line.replace('[', '').replace(']', '').rstrip(',')

        clean_line = clean_line.replace("'", "").replace('"', '').replace('‘', '').replace('’', '')

        row = [cell.strip() for cell in clean_line.split(',')]
        
        grid.append(row)

    target_color = grid[start_r][start_c]
    
    if target_color != replacement_color:
        queue = deque([(start_r, start_c)])
        grid[start_r][start_c] = replacement_color
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            r, c = queue.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < height and 0 <= nc < width:
                    if grid[nr][nc] == target_color:
                        grid[nr][nc] = replacement_color
                        queue.append((nr, nc))

    with open(output_file, 'w', encoding='utf-8') as f:
        for row in grid:
            formatted_row = "[" + ", ".join(f"'{cell}'" for cell in row) + "]"
            f.write(formatted_row + '\n')