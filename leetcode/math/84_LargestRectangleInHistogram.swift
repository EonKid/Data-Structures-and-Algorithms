class Solution {
    

    func largestRectangleArea(_ heights: [Int]) -> Int {
        
        var size = heights.count
        var maxA = 0
        var stack: [Int] = [-1]
        
        for i in 0 ..< size{
            let currH = heights[i]
            while let last = stack.last, last != -1 && currH <= heights[last]{
                let pI = stack.popLast()!
                let h = heights[pI]
                let l = stack.last! 
                let w = i - l - 1
                let area = w * h
                maxA = max(area, maxA)
            }
            stack.append(i)
        }
        
        while let last = stack.last, last != -1 {
            let pI = stack.popLast()!
            let h = heights[pI]
            let l = stack.last! 
            let w = size - l - 1
            let area = w * h
            maxA = max(area, maxA)
        }
        return maxA
    }
    
    
}