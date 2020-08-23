// https://leetcode.com/problems/remove-invalid-parentheses/

class Solution {

    func removeInvalidParentheses(_ s: String) -> [String] {
          var strData = Array(s)
		  var results = [String]()
		  var seen = Set<String>()
		  var currentStr = [Character]()
		  var maxLen = Int.min

		  func dfs(_ index: Int, _ leftCount: Int, _ rightCount: Int, _ currentStr:  [Character]){
				  if index == strData.count{
					if leftCount == rightCount{
						if currentStr.count > maxLen{
							results = [String]()
							maxLen = currentStr.count
						}
						let current = String(currentStr)
                        if !seen.contains(current) && currentStr.count == maxLen{
								seen.insert(current)
								results.append(current)
						}
					}
					 return
				  }

				  if leftCount >= rightCount{
                    let current =  strData[index]

                    // non-parenthesis
					if current != "(" && current != ")" {
                        var currentStr = currentStr
                        currentStr.append(current)
						dfs(index + 1, leftCount, rightCount, currentStr)
					}else{

                        //skip
						dfs(index + 1, leftCount, rightCount, currentStr)

                        //add left
						if current == "("{
                           var currentStr = currentStr
                            currentStr.append(current)
							dfs(index + 1, leftCount + 1, rightCount, currentStr)
						}

                        //right
						if current == ")"{
                            var currentStr = currentStr
                            currentStr.append(current)
							dfs(index + 1, leftCount, rightCount + 1, currentStr)
						}

					}

				  }

		   }

			dfs(0, 0, 0, currentStr)

		  return results
    }

}
