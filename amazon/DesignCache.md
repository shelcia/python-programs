# Design Cache

> This is the first part of any system design interview, coming up with the features which the system should support. As an interviewee, you should try to list down all the features you can think of which our system should support. Try to spend around 2 minutes for this section in the interview. You can use the notes section alongside to remember what you wrote.

**Q: What is the amount of data that we need to cache?**

A: Let's assume we are looking to cache on the scale of Google or Twitter. The total size of the cache would be a few TBs.

**Q: What should be the eviction strategy?**

A: It is possible that we might get entries when we would not have space to accommodate new entries. In such cases, we would need to remove one or more entries to make space for the new entry.

**Q: What should be the access pattern for the given cache?**

A: There are majorly three kinds of caching systems :
Write through cache : This is a caching system where writes go through the cache and write is confirmed as success only if writes to DB and the cache BOTH succeed. This is really useful for applications which write and re-read the information quickly. However, write latency will be higher in this case as there are writes to 2 separate systems.
_Write around cache_ : This is a caching system where write directly goes to the DB. The cache system reads the information from DB incase of a miss. While this ensures lower write load to the cache and faster writes, this can lead to higher read latency incase of applications which write and re-read the information quickly.

_Write back cache_ : This is a caching system where the write is directly done to the caching layer and the write is confirmed as soon as the write to the cache completes. The cache then asynchronously syncs this write to the DB. This would lead to a really quick write latency and high write throughput. But, as is the case with any non-persistent / in-memory write, we stand the risk of losing the data incase the caching layer dies. We can improve our odds by introducing having more than one replica acknowledging the write ( so that we don’t lose data if just one of the replica dies)

## Estimation

This is usually the second part of a design interview, coming up with the estimated numbers of how scalable our system should be. Important parameters to remember for this section is the number of queries per second and the data which the system will be required to handle.
Try to spend around 5 minutes for this section in the interview.

_Total cache size_ : Let's say 30TB as discussed earlier.

**Q: What is the kind of QPS we expect for the system?**

A: This estimation is important to understand the number of machines we will need to answer the queries. For example, if our estimations state that a single machine is going to handle 1M QPS, we run into a high risk of high latency / the machine dying because of queries not being answered fast enough and hence ending up in the backlog queue.
Again, let's assume the scale of Twitter / Google. We can expect around 10M QPS if not more.

**Q: What is the number of machines required to cache?**

A: A cache has to be inherently of low latency. Which means all cache data has to reside in main memory.
A production level caching machine would be 72G or 144G of RAM. Assuming beefier cache machines, we have 72G of main memory for 1 machine. Min. number of machine required = 30 TB / 72G which is close to 420 machines.
Do know that this is the absolute minimum. Its possible we might need more machines because the QPS per machine is higher than we want it to be.
