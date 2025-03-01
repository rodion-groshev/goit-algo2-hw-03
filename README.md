## Task 1. Application of the maximum flow algorithm for goods logistics

> Develop a program to model a flow network for logistics of goods from warehouses to stores using the maximum flow
> algorithm. Analyze the results and compare them with theoretical knowledge.

#### Task description:

- Use the Edmonds-Carp algorithm to realize the maximum flow.
- The construction of the graph should correspond to the given structure with 20 vertices and the given bandwidths.

### Analysis of the obtained results

| Terminal   | Store    | Actual Flow (units) |
|------------|----------|---------------------|
| Terminal 1 | Store 1  | 15                  |
| Terminal 1 | Store 2  | 10                  |
| Terminal 1 | Store 3  | 20                  |
| Terminal 1 | Store 4  | 15                  |
| Terminal 1 | Store 5  | 10                  |
| Terminal 1 | Store 6  | 20                  |
| Terminal 1 | Store 7  | 15                  |
| Terminal 1 | Store 8  | 15                  |
| Terminal 1 | Store 9  | 10                  |
|            |          |                     |
| Terminal 2 | Store 4  | 10                  |
| Terminal 2 | Store 5  | 10                  |
| Terminal 2 | Store 6  | 10                  |
| Terminal 2 | Store 7  | 15                  |
| Terminal 2 | Store 8  | 15                  |
| Terminal 2 | Store 9  | 10                  |
| Terminal 2 | Store 10 | 20                  |
| Terminal 2 | Store 11 | 10                  |
| Terminal 2 | Store 12 | 15                  |
| Terminal 2 | Store 13 | 5                   |
| Terminal 2 | Store 14 | 10                  |

1. Q: Which terminals provide the largest flow of goods to stores?

   A: Both terminals provide the same flow of goods to the stores - 130 units each.


2. Q: Which routes have the lowest throughput and how does this affect the overall flow?

   A: The lowest throughput among all routes to stores:

    - Terminal 2 -> Store 13 (5 units).

   Routes with a capacity of 10 units:

    - Terminal 1 -> Store 2
    - Terminal 1-2 -> Store 5
    - Terminal 1-2 -> Store 9
    - Terminal 2 -> Store 11
    - Terminal 2 -> Store 14


3. Q: Which stores received the least amount of goods and can their supply be increased by increasing the capacity of
   certain routes?
   A: Stores with the lowest volume of deliveries:
    - Store 2
    - Store 5
    - Store 9
    - Store 11
    - Store 13
    - Store 14

   Opportunities to increase supply:

    - Storage 4 -> Store 13
    - Storage 1 -> Store 2
    - Storage 2 -> Store 5
    - Storage 3 -> Store 9
    - Storage 4 -> Store 11
    - Storage 4 -> Store 14
   

4. Q: Are there any bottlenecks that can be removed to improve the efficiency of the logistics network?

   A: 
   - Terminal 1-2 -> Storage 2. Increase flow to 25 units to meet the needs of the store 6.
   - Terminal 1-2 -> Storage 3. Increase flow to 20 units to meet the needs of the store 7.


## Task 2: Comparing the effectiveness of OOBTree and a dictionary for range queries

> Develop a program to store a large set of data about goods in two data structures - OOBTree and dict - and conduct a comparative analysis of their performance for performing range queries.