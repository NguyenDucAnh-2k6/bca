At the beginning of the semester, the head of a computer science department D have to assign courses to teachers in a balanced way. The department D has m teachers T={1,2,...,m} and n courses C={1,2,...,n}. Each teacher t∈T has a preference list which is a list of courses he/she can teach depending on his/her specialization. We known a list of pairs of conflicting two courses that cannot be assigned to the same teacher as these courses have been already scheduled in the same slot of the timetable. The load of a teacher is the number of courses assigned to her/him. How to assign nn courses to mm teacher such that each course assigned to a teacher is in his/her preference list, no two conflicting courses are assigned to the same teacher, and the maximal load is minimal. <br />
Input <br />
The input consists of following lines <br />
Line 1: contains two integer m and n (1≤m≤10, 1≤n≤30) <br />
Line i+1: contains an positive integer k and k positive integers indicating the courses that teacher i can teach (∀i=1,…,m) <br />
Line m+2: contains an integer k <br />
Line i+m+2: contains two integer i and j indicating two conflicting courses (∀i=1,…,k) <br />
Output <br />
The output contains a unique number which is the maximal load of the teachers in the solution found and the value -1 if not solution found. <br />
Example <br />
Input <br />
4 12 <br />
5 1 3 5 10 12 <br />
5 9 3 4 8 12 <br />
6 1 2 3 4 9 7 <br />
7 1 2 3 5 6 10 11 <br />
25 <br />
1 2 <br />
1 3 <br />
1 5 <br />
2 4 <br />
2 5 <br />
2 6 <br />
3 5 <br />
3 7 <br />
3 10 <br />
4 6 <br />
4 9 <br />
5 6 <br />
5 7 <br />
5 8 <br />
6 8 <br />
6 9 <br />
7 8 <br />
7 10 <br />
7 11 <br />
8 9 <br />
8 11 <br />
8 12 <br />
9 12 <br />
10 11 <br />
11 12 <br />

Output
3
