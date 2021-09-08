# DFS

* dfs란? 깊이 우선 탐색(Depth First Search)로서 하나의 깊이를 먼저 탐색하는 알고리즘

![출처: codeforce](https://codeforces.com/predownloaded/8d/be/8dbe5d89e58b67f3d8e4d8e0e8eb3358ba921b28.png)



* 하나의 노드를 계속 따라간 뒤 정점을 찍고 다시 돌아오는 방식을 계속 해야하므로 후입선출(LIFO) 구조의 stack을 사용

* ```python
  def dfs(s, g, v, adj):
      stack = []
      visit = [0] * (v + 1)
      n = s  # 현재 방문한 정점
      visit[n] = 1
      # 방문한 정점에서 할 일
      while n > 0:  # 방문한 정점이 존재하면....
          # 현재 정점에서 방문하지 않은 정점 w찾기
          for w in range(1, V + 1):
              if adj[n][w] == 1 and visit[w] == 0:  # w가 n에 인접하고 미방문이면.....
                  stack.append(n)  # 현재 위치 경로로 저장
                  n = w  # w로 경로 이동
                  visit[w] = 1
                  if n == g:  # 현재 정점이 도착점과 같으면 1을 반환
                      return 1
                  break  # 현재 n을 기준으로 다시 w찾기
          else:  # w를 못찾은 경우, 지나온 정점을 꺼내 그 정점의 다른 w검색
              if stack:
                  n = stack.pop()
              else:
                  n = 0
      return 0
  
  T = int(input())
  for t in range(1, T + 1):
      V, E = map(int, input().split())  # 마지막 정점, 간선의 개수
      adj = [[0] * (V + 1) for _ in range(V + 1)]  # 인접 행렬
      for _ in range(E):
          n1, n2, = map(int, input().split())
          adj[n1][n2] = 1
          # adj[n2][n1] = 1 # 이 친구는 방향성 그래프가 없을 때
  
      S, G = map(int, input().split())
      ans = dfs(S, G, V, adj)
      print(f'#{t} {ans}')
  ```

* 만약, 노드 간의 방향성이 존재하게 된다면

* ```python
  for t in range(1, 11):
      T, L = map(int, input().split())    # tc와 해당 길이를 입력 받습니다.
      arr = list(map(int, input().split()))   # 하ㅏㄴ의 긴 줄을 입력
      maps = [[] for _ in range(100)] # 각 노드 별 연결되어있는 노드를 표시할 리스트
      visit = [False] * 100   # 방문기록을 남길 리스트
      stack = []  # 방문한 노드의 값을 저장할 리스트
      s = 0   # 처음 출발하게 되는 노드
  
      # arr에서 두개씨 나누어 출발 노드에 도착 노드를 삽입합니다.
      for start in range(0, len(arr), 2):
          maps[arr[start]].append(arr[start + 1])
  
      # 처음 가게 되는 노드를 저장하고 발자취를 남김니다.
      stack.append(s)
      visit[s] = True
  
      # stack이 다 떨어질때까지 반복
      while stack:
          # 도착지점인 99번 노드와 출발 노드가 같으면 while문 탈출
          if s == 99:
              print(f'#{t} 1')
              break
          # 그렇지 않으면, 계속 순환
          else:
              # 출발노드에서 도착노드가 존재하고 방문하지 않았으면 도착노드를 stack에 저장
              for i in maps[s]:
                  if not visit[i]:
                      visit[i] = True
                      stack.append(i)
              s = stack.pop()
      else:
          print(f'#{t} 0')
  ```

* 위와 같은 형식으로 코드를 구현해 나갑니다.