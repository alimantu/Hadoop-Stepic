Short overview of the tasks   
In case we use Hadoop Streaming => all the spaces between values in the input/output in the Mappers/Reducers are the tabulation characters(*'\t'*)   
**p2t1** - Native Dijkstra   
**Sample Input:**   
4 8   
1 2 6   
1 3 2   
1 4 10   
2 4 4   
3 1 5   
3 2 3   
3 4 8   
4 2 1   
1 4   
**Sample Output:**   
9   
   
**p2t2** - Mapper for the shortest path problem   
**Sample Input:**   
1	0	{2,3,4}   
2	1	{5,6}   
3	1	{}   
4	1	{7,8}   
5	INF	{9,10}   
6	INF	{}   
7	INF	{}   
8	INF	{}   
9	INF	{}   
10	INF	{}   
**Sample Output:**   
1	0	{2,3,4}   
2	1	{}   
3	1	{}   
4	1	{}   
2	1	{5,6}   
5	2	{}   
6	2	{}   
3	1	{}   
4	1	{7,8}   
7	2	{}   
8	2	{}   
5	INF	{9,10}   
9	INF	{}   
10	INF	{}   
6	INF	{}   
7	INF	{}   
8	INF	{}   
9	INF	{}   
10	INF	{}   
   
**p2t3** - Mapper for the shortest path problem   
**Sample Input:**   
1	0	{2,3,4}   
10	INF	{}   
10	INF	{}   
2	1	{}   
2	1	{5,6}   
3	1	{}   
3	1	{}   
4	1	{}   
4	1	{7,8}   
5	2	{}   
5	INF	{9,10}   
6	2	{}   
6	INF	{}   
7	2	{}   
7	INF	{}   
8	2	{}   
8	INF	{}   
9	INF	{}   
9	INF	{}   
**Sample Output:**   
1	0	{2,3,4}   
10	INF	{}   
2	1	{5,6}   
3	1	{}   
4	1	{7,8}   
5	2	{9,10}   
6	2	{}   
7	2	{}   
8	2	{}   
9	INF	{}  
   
**p3t1** - Mapper for the PageRank problem   
**Sample Input:**   
1	0.200	{2,4}   
2	0.200	{3,5}   
3	0.200	{4}   
4	0.200	{5}   
5	0.200	{1,2,3}   
**Sample Output:**   
1	0.200	{2,4}   
2	0.100	{}   
4	0.100	{}   
2	0.200	{3,5}   
3	0.100	{}   
5	0.100	{}   
3	0.200	{4}   
4	0.200	{}   
4	0.200	{5}   
5	0.200	{}   
5	0.200	{1,2,3}   
1	0.067	{}   
2	0.067	{}   
3	0.067	{}   
   
**p3t2** - Reducer for the PageRank problem   
**Sample Input:**   
1	0.067	{}   
1	0.200	{2,4}   
2	0.067	{}   
2	0.100	{}   
2	0.200	{3,5}   
3	0.067	{}   
3	0.100	{}   
3	0.200	{4}   
4	0.100	{}   
4	0.200	{}   
4	0.200	{5}   
5	0.100	{}   
5	0.200	{}   
5	0.200	{1,2,3}   
**Sample Output:**   
1	0.067	{2,4}   
2	0.167	{3,5}   
3	0.167	{4}   
4	0.300	{5}   
5	0.300	{1,2,3}   
   
**p3t3** - Reducer for the PageRank problem(with respect to the random transfer of the user)   
**Sample Input:**   
1	0.067	{}   
1	0.200	{2,4}   
2	0.067	{}   
2	0.100	{}   
2	0.200	{3,5}   
3	0.067	{}   
3	0.100	{}   
3	0.200	{4}   
4	0.100	{}   
4	0.200	{}   
4	0.200	{5}   
5	0.100	{}   
5	0.200	{}   
5	0.200	{1,2,3}   
**Sample Output:**   
1	0.080	{2,4}   
2	0.170	{3,5}   
3	0.170	{4}   
4	0.290	{5}   
5	0.290	{1,2,3}   
