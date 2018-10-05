# RandoRouteFinder

RandoRouteFinder is an item tracker and route suggestor for [A Link To The Past Randomizer](https://alttpr.com/).

It models the game world with a graph, where each node represents an atomic Region and each edge (or Gate) is enriched with item Requisites for traversing from one region to another. Many Gates have multiple possible Requisites, so a Gate is considered "open" if any of the requisites are satisfied. As the user plays the game they can add or remove an item from the Inventory, which will update the requisites of all the Gates in the graph. The plan is to include a game map which shows which Regions are accessible from the root and which are not.