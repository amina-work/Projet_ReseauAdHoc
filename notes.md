### MANET AODV Reactive Routing Protocol

Pros:
=> On-Demand Routing Protocols.
=> The route is determined when needed (Reactive).
=> The paths remain identical until a packet forwarding error occurs, i.e. a change in the network topology means that the packet is not transferable anymore.

Cons:
=> Reactive to network topology changes more slowly than a proactive protocol.

### Setting-up the Nodes and the Neighbors
MANET comprises of nodes that communicate each other directly or indirectly by employing other nodes as routers in the case of they are not located within the communication range. In this assignment, a node carries three different information: location, transmission range, residual battery level (eneregy).

In order to determine neighborhood of each node, it is first needed to examine the location and transmission range information. 