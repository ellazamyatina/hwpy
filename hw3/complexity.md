1. Brute force solution

   O(n! * n^2)

   Explanation: we use permutations(n!) and in each permutation do double cycle check(n^2)


2. Recursive function
   
   O(n!)
   
   In the each level of recursion try to place queen on the n position and dont touch useless variants. At worst use n!.


3. Optimized solution
   
   O(n!)

   I solved this task by using sets.
