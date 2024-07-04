class Solution:
    def spiralOrder(self, matrix):
        seen = set()
        ret =[]
        self.traverse_matrix((0, 0), "r", matrix, seen, ret)
        return ret
    
    # input: coordinates, curr_direction
    # output: None
    # this function with traverse the entire matrix
    def traverse_matrix(self, coord, direction, matrix, seen, ret):
        i, j = coord
        # check bounds
        not_in_boundary = i < 0 or i > len(matrix) - 1 or j < 0 or j > len(matrix[0]) - 1
        in_seen = coord in seen

        if len(matrix) * len(matrix[0]) == len(seen):
            return

        if not_in_boundary or in_seen:
            match direction:
                case "r":
                    self.traverse_matrix((i + 1, j - 1), "d", matrix, seen, ret)
                case "d":
                    self.traverse_matrix((i - 1, j - 1), "l", matrix, seen, ret)
                case "l":
                    self.traverse_matrix((i - 1, j + 1), "u", matrix, seen, ret)
                case "u":
                    self.traverse_matrix((i + 1, j + 1), "r", matrix, seen, ret)

        else:
            # continue in that direction
            seen.add(coord)
            ret.append(matrix[i][j])
            match direction:
                case "r":
                    self.traverse_matrix((i, j + 1), "r", matrix, seen, ret)
                case "d":
                    self.traverse_matrix((i + 1, j), "d", matrix, seen, ret)
                case "l":
                    self.traverse_matrix((i, j - 1), "l", matrix, seen, ret)
                case "u":
                    self.traverse_matrix((i - 1, j), "u", matrix, seen, ret)



a = Solution()

input = [[1,2,3],[4,5,6],[7,8,9]]


print(a.spiralOrder(input))