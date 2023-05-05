# Multy Agents and Clips creator

from os import listdir
from os.path import isfile, isdir
import hou

def ls(path):    
    return [obj for obj in listdir(path)]
    
def ls2(path):    
    return [obj for obj in listdir(path) if isfile(path + obj)]
    
node = hou.node("/obj/Crowds")

path = "Animations/"
pos = (0,0)

for person in ls(path):
    pathFile = path[0:-1]+"/"+person+"/T-Pose.fbx"
    
    # Creacio del Agent
    
    agenNode = node.createNode("agent", "Agent_"+person)
    agenNode.setPosition(pos)
    agenNode.setParms({
        "agentname": person, 
        "input":"fbx",
        "fbxfile":pathFile
        })
    # Creacio del node de Clips per cada personatge:

    agenClipNode = node.createNode("agentclip::2.0", "AgentClip_"+person)
    agenNode.setPosition((agenNode.position()[0], agenNode.position()[1]+1))
     
    pos = (pos[0]+4,pos[1])
    # conecta Nodes d' Agent i clips
    agenClipNode.setFirstInput(agenNode)
    
    # Coneccio de clips:

    pathAnimation = path[0:-1]+"/"+person+"/"
    
    files = ls2(pathAnimation)
    num = len(files)
    agenClipNode.parm("clips").set(num)
    
    n = 1
    for animation in files:
        agenClipNode.setParms({
            "name"+str(n):animation[0:-4],
            "source"+str(n):1,
            "file"+str(n):pathAnimation+"/"+animation,
            "converttoinplace"+str(n):1
            })
        n = n + 1
    
    
    
    
