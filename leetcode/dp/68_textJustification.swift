//https://leetcode.com/problems/text-justification/


class Solution {
    func fullJustify(_ words: [String], _ maxWidth: Int) -> [String] {
        var arrResult = [String]()
        var i = 0
        var j = 0
    while i < words.count{
       j = i
       var lengthS = words[i].count
       var lengthW = words[i].count
       j += 1
       while j < words.count && 1 + lengthS + words[j].count <= maxWidth {
        lengthS += 1 + words[j].count
        lengthW += words[j].count
        j += 1
    }
   let gap = j - i - 1
   let spaces = maxWidth - lengthW
   var line = words[i]
   if gap > 0{
     var base = (j == words.count) ? 1 : (spaces / gap)
     var mod = (j == words.count) ? 0 : (spaces % gap)
       i += 1
       while i < j {
           var modString = ""
           if mod > 0{
               modString = " "
           }
           line += String(repeating:" ", count: base) + modString + words[i]
           i += 1
           mod -= 1
       }
    }
   let lastLine = maxWidth - line.count
   if lastLine > 0{
       line += String(repeating: " ", count: lastLine)
   }
   arrResult.append(line)
   i = j

   }
    return arrResult
    }

}




