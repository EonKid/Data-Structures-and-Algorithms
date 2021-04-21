// https://leetcode.com/problems/max-points-on-a-line/

class Solution {

    func getGcd(_ x: Int,_ y: Int) -> Int{
        return (y == 0) ? x : self.getGcd(y, (x % y))
    }

    func getSlope(_ p1: [Int],_ p2: [Int]) -> String{
         var x = p2[0] - p1[0]
         var y = p2[1] - p1[1]
          
         let gcd = self.getGcd(x, y)
         x = (gcd == 0) ? (x / max(x, y)) : (x / gcd)
         y = (gcd == 0) ? (y / max(x, y)) : (y / gcd)

         return "\(x),\(y)"
    }


    func maxPoints(_ points: [[Int]]) -> Int {
        if points.count < 3 {
            return points.count
        }
        var maxCount = 2

        for i in stride(from: 0, to: points.count, by: 1){

            var mapStore = [String: Int]()

            for j in stride(from: i + 1, to: points.count, by: 1){
                var slope = self.getSlope(points[i], points[j])
                if let count = mapStore[slope]{
                    mapStore[slope] = count + 1
                }else {
                    mapStore[slope] = 1
                }
            }

            for (slope, count) in mapStore{
                maxCount = max(maxCount, count + 1)
            }
        }

        return maxCount
        
    }
}