
//https://leetcode.jp/problemdetail.php?id=1245

class Solution {

    func treeDiameter(_ edges: [[Int]]) -> Int {
        var g = Array.init(repeating: [Int](), count: edges.count+1)
        for data in edges{
            let u = data[0]
            let v = data[1]
            g[u].append(v)
            g[v].append(u)
        }
        let nodeLong = bfs(g, n: (0,0))
        let nodeLongest = bfs(g, n: (nodeLong.0, 0))
        return nodeLongest.1
    }

    /**
           Time complexity: O((V+U))
     */
    func bfs( _ edges: [[Int]], n:(Int, Int)) -> (Int, Int){
        var visited = Set<Int>()
        var aQueue = [(Int, Int)]()
        aQueue.append(n)
        var node = n
        while !aQueue.isEmpty {
            node = aQueue.first!
            let u = node.0
            aQueue.remove(at: 0)
            visited.insert(u)

            for v in edges[u] {
                if !visited.contains(v) {
                    aQueue.append((v,node.1 + 1))
                }
            }

        }
        return node
    }

}



var maxLength = 0
let edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
//let edges = [[0,1],[0,2]]

let sol = Solution()
print("Diameter of tree: \(sol.treeDiameter(edges))")
