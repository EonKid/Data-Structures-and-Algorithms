class Solution {
    
    func reconstructQueue(_ people: [[Int]]) -> [[Int]] {
        let people = people.sorted{ (person1, person2) in 
            if person1[0] == person2[0] {
                return person1[1] < person2[1]
            }
            return person1[0] > person2[0]
        }
                
        var result = [[Int]]()
        
        for person in people {
            result.insert(person, at: person[1])
        }
        return result
    }
    
}