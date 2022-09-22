import os

class ASTBlock:
    BLK_MAIN = 1
    BLK_IF = 2
    BLK_ELSE = 3
    BLK_ELIF = 4
    BLK_TRY = 5
    BLK_CONTAINER = 6
    BLK_EXCEPT = 7
    BLK_FINALLY = 8
    BLK_WHILE = 9
    BLK_FOR = 10
    BLK_WITH = 11
    BLK_ASYNCFOR = 12

    def __init__(self, blktype):
        self.blktype = blktype
        self.ast_nodes = []

    def append(self, node):
        self.ast_nodes.append(node)

class ASTObject:
    def __init__(self, obj):
        self.object = obj
    def __repr__(self) -> str:
        return 'ASTObject(%s)' %self.object

class ASTImport:
    def __init__(self, name, fromlist):
        self.name = name
        self.fromlist = fromlist
    def __repr__(self) -> str:
        return 'ASTImport(%s, %s)' %(self.name, self.fromlist)

class ASTStore:
    def __init__(self, src_node, dest_node):
        self.src_node = src_node
        self.dest_node = dest_node
    def __repr__(self) -> str:
        return 'ASTStore(%s->%s)' %(self.src_node, self.dest_node)

class ASTName:
    def __init__(self, name):
        self.name = name
    def __repr__(self) -> str:
        return 'ASTName(%s)'%self.name

'''only placeholder'''
class ASTFunction:
    def __init__(self):
        pass
    def __repr__(self) -> str:
        return 'ASTFunction()'
class DecompileContext:
    def __init__(self):
        self.stack = []
        self.stack = []
        self.blocks = []
        self.defblock = ASTBlock(ASTBlock.BLK_MAIN)
        self.curblock = self.defblock
        self.blocks.append(self.defblock)

class ASTReturn:
    def __init__(self, value) -> None:
        self.value = value