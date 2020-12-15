// https://leetcode.com/problems/friend-circles/

class Solution {

    func dfs(_ M: [[Int]], _ visited: inout [Bool], _ current: Int){
        if visited[current]{
            return
        }
        visited[current] = true
        for col in 0 ..< M[current].count{
            if !visited[col] && M[current][col] == 1{
                dfs(M, &visited, col)
            }
        }

    }

    func findCircleNum(_ M: [[Int]]) -> Int {
        var count = 0
        let N = M.count
        var visited = Array.init(repeating: false, count: N)
        for row in 0 ..< N{
            if !visited[row]{
                dfs(M, &visited, row)
                count += 1
            }
        }
        return count
    }
}