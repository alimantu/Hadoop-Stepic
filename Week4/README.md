Short tasks overview   
Week 4:   
**p1t1** - In-mapper combining v.1 for Hadoop WordCount   
   
**p1t2** - In-mapper combining v.2 for Hadoop WordCount   
   
**p1t3** - Reducer for calculating the avg time spent by user on site(Input - sorted *key + '\t' + value*)   
   
**p1t4** - Combiner for aggregating the time and number of vizits per site by user(Input - sorted *key + '\t' + value + ';' + vizitsCount*)   
   
**p1t5** - Mapper for phase 1 Distinct Values v1   
**Sample Input:**   
1 a,b   
2	a,d,e   
1	b   
3	a,b   
**Sample Output:**   
1,a	1   
1,b	1   
2,a	1   
2,d	1   
2,e	1   
1,b	1   
3,a	1   
3,b	1   
   
**p1t6** - Reducer for phase 1 Distinct Values v1   
**Sample Input:**   
1,a	1   
1,b	1   
1,b	1   
2,a	1   
2,d	1   
2,e	1   
3,a	1   
3,b	1   
**Sample Output:**   
1,a   
1,b   
2,a   
2,d   
2,e   
3,a   
3,b   
   
**p1t7** - Mapper for phase 2 Distinct Values v1   
**Sample Input:**   
1,a   
2,a   
3,a   
1,b   
3,b   
2,d   
2,e   
**Sample Output:**   
a	1   
a	1   
a	1   
b	1   
b	1   
d	1   
e	1   
   
**p1t8** - Reducer for  phase 2 Distinct Values v2   
**Sample Input:**   
1	a   
1	b   
1	b   
2	a   
2	d   
2	e   
3	a   
3	b   
**Sample Output:**   
a	3   
d	1   
b	2   
e	1   
   
**p1t9** - Mapper for Cross-Correlation(using pairs)   
**Sample Input:**   
a b   
a b a c   
**Sample Output:**   
a,b	1   
b,a	1   
a,b	1   
a,c	1   
b,a	1   
b,a	1   
b,c	1   
a,b	1   
a,c	1   
c,a	1   
c,b	1   
c,a	1   
   
**p1t10** - Mapper for Cross-Correlation(using stripes)   
**Sample Input:**   
a b   
a b a c   
**Sample Output:**   
a	b:1   
b	a:1   
a	b:1,c:1   
b	a:2,c:1   
a	b:1,c:1   
c	b:1,a:2   
