from routemin import create_graph, calculate_shortest_path, main

# グラフを作成
G = create_graph()

# 最短経路を計算
start_station = '三鷹'
end_station = '大崎'
include_dash = False
path, total_time, compact_lines = calculate_shortest_path(G, start_station, end_station, include_dash)

# 最短経路を矢印を使って表示
formatted_path = ' → '.join(path)
print(f"最短経路: {formatted_path}")
print(f"合計時間: {total_time}", "minutes")
