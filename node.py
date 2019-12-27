

class Node:
    positionMoves = [[1, 3], [1, 3, -1], [3, -1], [-3, 3, 1], [-3, 1, 3, -1],
                     [-3, 3, -1], [-3, 1], [-3, 1, -1], [-3, -1]]

    def __init__(self):
        self.goal = [5, 6, 7, 4, 0, 8, 3, 2, 1]
        self.board = [1, 2, 3, 8, 0, 4, 7, 6, 5]
        self.parent = 0
        self.action = 0
        self.f = 0
        self.g = 0
        self.searchType = 0

    def misplaced(self):
        d = 0
        temp = zip(self.board, self.goal)
        for i in temp:
            if i[0] != i[1]:
                d = d + 1
        return d

    def manhattan(self):
        d = 0
        for i in range(9):
            if i != 0:
                d = d + abs(self.board.index(i) - self.goal.index(i))
        return d

    def initial_search_value(self):
        if self.searchType in [0,2]:
            self.f = self.misplaced()
        elif self.searchType in [1,3]:
            self.f = self.manhattan()
        self.g = self.misplaced()

    def parity(self, array):
        counter1 = len(array)
        par = 0
        for i in reversed(range(1, counter1)):
            if array[i] == 0:
                pass
            else:
                for j in reversed(range(0, i)):
                    if array[j] != 0 and array[j] > array[i]:
                        par += 1
        return par

    def parityCompare(self, array1, array2):
        return not ((self.parity(array1) + self.parity(array2)) % 2)

    def move(self, queue, closed):
        counter = 0
        # print(queue[0].board)
        while queue:
            if queue[0].board in closed:
                queue.pop(0)
            blank = queue[0].board.index(0)
            for i in Node.positionMoves[blank]:
                # print("i", i, Node.positionMoves[blank])
                new_board = list(queue[0].board)
                # print("old", new_board)
                new_board[blank], new_board[blank + i] = new_board[blank + i], new_board[blank]
                # print("new", new_board)
                if new_board not in closed and new_board:
                    child = Node()
                    child.parent = queue[0]
                    child.goal = queue[0].goal
                    child.action = i
                    child.g = queue[0].g - 1
                    child.board = new_board
                    child.searchType = queue[0].searchType
                    # print("Closed", len(closed))

                    if child.board == child.goal:
                        return child
                    else:
                        if child.searchType == 0:
                            child.f = child.misplaced()
                        elif child.searchType == 1:
                            child.f = child.manhattan()
                        elif child.searchType == 2:
                            child.f = child.misplaced() + child.g
                        elif child.searchType == 3:
                            child.f = child.manhattan() + child.g
                    queue.append(child)
            closed.append(queue.pop(0).board)
            temp = min(queue, key=lambda x: x.f)
            queue.remove(temp)
            queue = [temp] + queue

            if not queue:
                return
            else:
                pass
        print("Total Nodes Expanded: ", len(closed))

    def path(self):
        array = []
        temp = self
        while temp.parent:
            array = [temp.action] + array
            temp = temp.parent
        return array

    def directions(self, array):
        temp = array
        for i in range(len(array)):
            if array[i] == -3:
                temp[i] = "Up"
            elif array[i] == 3:
                temp[i] = "Down"
            elif array[i] == -1:
                temp[i] = "Right"
            elif array[i] == 1:
                temp[i] = "Left"
            else:
                pass
        return temp
