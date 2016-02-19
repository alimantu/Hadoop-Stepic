Short tasks overview   
In case we use Hadoop Streaming => all the spaces between values in the input/output in the Mappers/Reducers are the tabulation characters(*'\t'*)   
   
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
   
**p2t1**  - Mapper for filtering   
**Sample Input:**   
1448713968	user2	https://ru.wikipedia.org/   
1448764519	user10	https://stepic.org/   
1448713968	user5	http://google.com/   
1448773411	user10	https://stepic.org/explore/courses   
1448709864	user3	http://vk.com/   
**Sample Output:**   
1448764519	user10	https://stepic.org/   
1448773411	user10	https://stepic.org/explore/courses   
   
**p2t2** - Mapper for resolving only part of the input information   
**Sample Input:**   
1448713968	user2	https://ru.wikipedia.org/   
1448764519	user10	https://stepic.org/   
1448713968	user5	http://google.com/   
1448773411	user10	https://stepic.org/explore/courses   
1448709864	user3	http://vk.com/   
**Sample Output:**   
https://ru.wikipedia.org/   
https://stepic.org/   
http://google.com/   
https://stepic.org/explore/courses   
http://vk.com/   
   
**p2t3** - Reducer for uniting the input sets   
**Sample Input:**   
1	A   
2	A   
2	B   
3	B   
**Sample Output:**   
1   
2   
3   
   
**p2t4** - Reducer for set intersectioning   
**Sample Input:**   
1	A   
2	A   
2	B   
3	B   
**Sample Output:**   
2   
   
**p2t5** - Reducer for set complementing   
**Sample Input:**   
1	A   
2	A   
2	B   
3	B   
**Sample Output:**   
1   
   
**p2t6** - Reducer for set simetrical complementing   
**Sample Input:**   
1	A   
2	A   
2	B   
3	B   
**Sample Output:**   
1   
3   
   
**p2t7** - Reducer for joining two input queries by user id   
**Sample Input:**
user1	query:гугл   
user1	url:google.ru   
user2	query:стэпик   
user2	query:стэпик курсы   
user2	url:stepic.org   
user2	url:stepic.org/explore/courses   
user3	query:вконтакте   
**Sample Output:**   
user1	гугл	google.ru   
user2	стэпик	stepic.org   
user2	стэпик	stepic.org/explore/courses   
user2	стэпик курсы	stepic.org   
user2	стэпик курсы	stepic.org/explore/courses   
   
**p3t1** - Mapper for first part of the TF-IDF problem   
**Sample Input:**   
1:aut Caesar aut nihil   
1:aut aut   
2:de mortuis aut bene aut nihil   
**Sample Output:**   
aut#1	1   
Caesar#1	1   
aut#1	1   
nihil#1	1   
aut#1	1   
aut#1	1   
de#2	1   
mortuis#2	1   
aut#2	1   
bene#2	1   
aut#2	1   
nihil#2	1   
   
**p3t2** - Reducer for the first part of the TF-IDF problem   
**Sample Input:**   
aut#1	1   
aut#1	1   
aut#1	1   
aut#1	1   
aut#2	1   
aut#2	1   
bene#2	1   
de#2	1   
mortuis#2	1   
nihil#1	1   
nihil#2	1   
Caesar#1	1   
**Sample Output:**   
aut	1	4   
aut	2	2   
bene	2	1   
de	2	1   
mortuis	2	1   
nihil	1	1   
nihil	2	1   
Caesar	1	1   
   
**p3t3** - Mapper for the second part of the TF-IDF problem   
**Sample Input:**   
aut	1	4   
aut	2	2   
bene	2	1   
de	2	1   
mortuis	2	1   
nihil	1	1   
nihil	2	1   
Caesar	1	1   
**Sample Output:**   
aut	1;4;1   
aut	2;2;1   
bene	2;1;1   
de	2;1;1   
mortuis	2;1;1   
nihil	1;1;1   
nihil	2;1;1   
Caesar	1;1;1   
   
**p3t4** - Reducer for the second part of the TF-IDF problem   
**Sample Input:**
aut	1;4;1   
aut	2;2;1   
bene	2;1;1   
de	2;1;1   
mortuis	2;1;1   
nihil	1;1;1   
nihil	2;1;1   
Caesar	1;1;1   
**Sample Output:**   
aut#1	4	2   
aut#2	2	2   
bene#2	1	1   
de#2	1	1   
mortuis#2	1	1   
nihil#1	1	2   
nihil#2	1	2   
Caesar#1	1	1   
