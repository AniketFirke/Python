from collections import deque

def calc_erdos(adj_lst):
    erdos_numbers = {}
    queue = deque()
    queue.append(('Erdos, P.', 0))
    while queue:
        cur_author, dist = queue.popleft()
        if cur_author not in erdos_numbers:
            erdos_numbers[cur_author] = dist
        for author in adj_lst[cur_author]:
            if author not in erdos_numbers:
                queue.append((author, dist+1))
    return erdos_numbers

def main():
    num_scenario = int(input())
    input() # Read blank line
    for idx_scenario in range(1, num_scenario+1):
        num_papers, num_queries = [int(num) for num in input().split()]
        adj_lst = {}
        for _ in range(num_papers):
            paper = input()
            authors, title = paper.split(':')
            authors = [author.strip() for author in authors.split(',')]
            authors = [', '.join(first_last) for first_last in zip(authors[::2], authors[1::2])]
            # Build the adjacency list
            for author in authors:
                author_neighbors = adj_lst.get(author, set())
                for coauthor in authors:
                    if coauthor == author:
                        continue
                    author_neighbors.add(coauthor)
                adj_lst[author] = author_neighbors
        erdos_numbers = calc_erdos(adj_lst)
        print(f'Scenario {idx_scenario}')
        for _ in range(num_queries):
            author = input()
            print(f'{author} {erdos_numbers.get(author, "infinity")}')
if __name__ == '__main__':
    main()
