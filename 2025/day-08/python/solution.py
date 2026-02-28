import math

Point = tuple[int,int,int]

def get_point_pairs(data:list[str]) -> list[tuple[Point,Point,int]]:
  points:list[list[str]] = [line.strip().split(',') for line in data]
  points:list[Point] = [(int(x), int(y), int(z)) for [x, y, z] in points]
  points_length = len(points)

  pairs:list[tuple[Point,Point,int]] = []
  for i in range(points_length):
    for j in range(i + 1, points_length):
      point1, point2 = points[i], points[j]
      distance = math.dist(point1, point2)
      pairs.append((point1, point2, distance))

  return sorted(pairs, key=lambda x: x[2])

def merge_circuits(circuits:list[set[Point]]) -> None:
  merged = True
  while merged:
    merged = False
    for i in range(len(circuits)):
      for j in range(i + 1, len(circuits)):
        if circuits[i] & circuits[j]:
          circuits[i] |= circuits[j]
          circuits.pop(j)
          merged = True
          break

def part1(data:list[str], limit:int) -> int:
  closest_pairs = get_point_pairs(data)[:limit]
  circuits:list[set[Point]] = []
  for point1, point2, _ in closest_pairs:
    pair_added_to_circuit = False
    for circuit in circuits:
      if point1 in circuit or point2 in circuit:
        circuit |= {point1, point2}
        pair_added_to_circuit = True
        break

    if not pair_added_to_circuit:
      circuits.append({point1, point2})

  merge_circuits(circuits)
  three_largest_circuits = sorted([len(circuit) for circuit in circuits])[::-1][:3]
  return math.prod(three_largest_circuits)

def add_pair_to_circuits(pair:tuple[Point, Point, int], circuits:list[list[Point]]) -> bool:
  point1, point2, _ = pair
  for circuit in circuits:
    if point1 == circuit[0]:
      if point2 not in circuit:
        circuit.insert(0, point2)
      return True
    if point2 == circuit[0]:
      if point1 not in circuit:
        circuit.insert(0, point1)
      return True
    if point1 == circuit[-1]:
      if point2 not in circuit:
        circuit.append(point2)
      return True
    if point2 == circuit[-1]:
      if point1 not in circuit:
        circuit.append(point1)
      return True

  return False

def do_merge_circuits(circuits:list[list[Point]]) -> None:
  merged = True
  while merged:
    merged = False
    for i in range(len(circuits)):
      for j in range(i + 1, len(circuits)):

        # если начало цепи[i] совпадает с концом цепи[j]
        if circuits[i][0] == circuits[j][-1]:
          if circuits[i][-1] in circuits[j]:
            print('absorb', f"({i})", circuits[i], 'by', f"({j})", circuits[j])
            circuits.pop(i)
          elif circuits[j][0] in circuits[i]:
            print('absorb', f"({j})", circuits[j], 'by', f"({i})", circuits[i])
            circuits.pop(j)
          else:
            print('merge', f"({j})", circuits[j], '+', f"({i})", circuits[i])
            merged_circuit = circuits[j] + circuits[i][1:]
            circuits.pop(j)
            circuits.pop(i)
            circuits.append(merged_circuit)
          merged = True
          break

        # если конец цепи[i] совпадает с началом цепи[j]
        if circuits[i][-1] == circuits[j][0]:
          if circuits[i][0] in circuits[j]:
            print('absorb', f"({i})", circuits[i], 'by', f"({j})", circuits[j])
            circuits.pop(i)
          elif circuits[j][-1] in circuits[i]:
            print('absorb', f"({j})", circuits[j], 'by', f"({i})", circuits[i])
            circuits.pop(j)
          else:
            print('merge', f"({i})", circuits[i], '+', f"({j})", circuits[j])
            merged_circuit = circuits[i] + circuits[j][1:]
            circuits.pop(j)
            circuits.pop(i)
            circuits.append(merged_circuit)
          merged = True
          break

        # если совпали начала обоих цепей
        if circuits[i][0] == circuits[j][0]:
          if circuits[i][-1] in circuits[j]:
            print('absorb', f"({i})", circuits[i], 'by', f"({j})", circuits[j])
            circuits.pop(i)
          elif circuits[j][-1] in circuits[i]:
            print('absorb', f"({j})", circuits[j], 'by', f"({i})", circuits[i])
            circuits.pop(j)
          else:
            print('merge', f"({j})(reverse)", circuits[j][::-1], '+', f"({i})", circuits[i])
            merged_circuit = circuits[j][1:][::-1] + circuits[i]
            circuits.pop(j)
            circuits.pop(i)
            circuits.append(merged_circuit)
          merged = True
          break

        # если совпали концы обоих цепей
        if circuits[i][-1] == circuits[j][-1]:
          if circuits[i][0] in circuits[j]:
            print('absorb', f"({i})", circuits[i], 'by', f"({j})", circuits[j])
            circuits.pop(i)
          elif circuits[j][0] in circuits[i]:
            print('absorb', f"({j})", circuits[j], 'by', f"({i})", circuits[i])
            circuits.pop(j)
          else:
            print('merge', f"({i})", circuits[i], '+', f"({j})(reverse)", circuits[j][1:][::-1])
            merged_circuit = circuits[j] + circuits[i][1:][::-1]
            circuits.pop(j)
            circuits.pop(i)
            circuits.append(merged_circuit)
          merged = True
          break

      if merged:
        break

def part2(data:list[str]) -> int:
  pairs = get_point_pairs(data)
  circuits:list[list[Point]] = []

  p = 0
  for pair in pairs:
    pair_added_to_circuit = add_pair_to_circuits(pair, circuits)

    if not pair_added_to_circuit:
      point1, point2, _ = pair
      circuits.append([point1, point2])

    p += 1
    print(f"{p}", pair[0], pair[1])
    for i in range(len(circuits)):
      print(i, circuits[i])

    # do_merge_circuits(circuits)

    print()

  return 0
