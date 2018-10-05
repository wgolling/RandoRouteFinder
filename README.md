# RandoRouteFinder

## Overview

RandoRouteFinder is intended to be an item tracker and route suggestor for the [Legend of Zelda: A Link To The Past Randomizer](https://alttpr.com/). Currently the basic graph objects and methods have been set up, and development is being done on an interface.

The Zelda franchise is based on exploration, and opening up more of the world by finding new items. This makes the games very amenable to shuffling the item locations, and A Link To The Past is a particularly popular game to randomize. An Item Tracker is a common program to use with randomizers: it allows you to keep track of the items you've found so far, and based on this the program determines which locations are accessible.

This project is just my version of an item tracker, written primarily to help me learn Python and GUI programming. The software models the game world as a graph, where each node is an atomic Region of the map and each edge (or Gate) is enriched with Requisite objects which indicate if it is traversable or not. Many Gates have different possible Requisites, so a Gate is considered "open" if any of its requisites are satisfied. As the user plays the game they can use the graphical interface to add or remove items from the Inventory, which will update the requisites of all the Gates in the graph as well as Region accessibilities. The plan is to extend this concept to a Route Suggester: based on your accessible regions and various properties about them, the program should give a ranked list of where it thinks you should go next, along with shortest paths to get there.

## Getting Started

The project is not finished yet, so not currently reccomended for use.