from gephistreamer import graph
from gephistreamer import streamer
import UserInteraction
from itertools import cycle

stream = streamer.Streamer(streamer.GephiWS(hostname="localhost", port=8080, workspace="workspace1"))
# Create a node with a custom_property
#node_a = graph.Node("A",custom_property=1)

def createUserGraph(listUsers):
    users2entityMatrix = UserInteraction.entity2User(listUsers[0],listUsers[1])
    userA = graph.Node(str(users2entityMatrix["UserA"].loc[0]))
    userB = graph.Node(str(users2entityMatrix["UserB"].loc[0]))
    #userA.color_hex(255,0,0)
    j = 0
    stream.add_node(userA,userB)
    stream.add_edge(graph.Edge(userA,userB))
    for i in users2entityMatrix["Entities"]:
        stream.add_node(graph.Node(str(i)))

    stream.commit()


listUsers = [17643749,18269496]
createUserGraph(listUsers)
#print(UserInteraction.entity2User(listUsers[0],listUsers[1])["Entities"])




# Create a node and then add the custom_property
#node_b = graph.Node("B")
#node_b.property['custom_property']=2
 #stream.add_node(node_b)
#stream.commit()
# Add the node to the stream
# you can also do it one by one or via a list
# l = [node_a,node_b]
# stream.add_node(*l)
#stream.add_node(node_a,node_b)


# Create edge
# You can also use the id of the node :  graph.Edge("A","B",custom_property="hello")
#edge_ab = graph.Edge(node_a,node_b,custom_property="hello")
#stream.add_edge(edge_ab)

#stream = streamer.Streamer(streamer.GephiREST(),auto_commit=False)
#[.. actions ..]
#stream.commit() # Will send all actions buffered to Gephi

