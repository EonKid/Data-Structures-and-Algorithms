/**
Towers
https://see.stanford.edu/materials/icspacs106b/Lecture09.pdf
n = number of disks
rods = source = A, destination = B, auxiliary = C

Time complexity: 2^n

**/

func moveTowers(_ n: Int, _ source: String, _ destination: String, _ auxiliary: String){
     if n > 0{
       moveTowers(n-1, source, auxiliary, destination)
       print("Move using disk \(n) from: \(source) to: \(destination)")
       moveTowers(n-1, auxiliary, destination, source)
     }

}
