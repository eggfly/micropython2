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


class ASTNodeList:
    def __init__(self, nodes) -> None:
        self.nodes = nodes

    def __repr__(self) -> str:
        return 'ASTNodeList(%s)' % self.nodes


class ASTObject:
    def __init__(self, obj):
        self.object = obj

    def __repr__(self) -> str:
        return 'ASTObject(%s)' % self.object


class ASTImport:
    def __init__(self, name, fromlist):
        self.name = name
        self.fromlist = fromlist

    def __repr__(self) -> str:
        return 'ASTImport(%s, %s)' % (self.name, self.fromlist)


class ASTStore:
    def __init__(self, src_node, dest_node):
        self.src_node = src_node
        self.dest_node = dest_node

    def __repr__(self) -> str:
        return 'ASTStore(%s->%s)' % (self.src_node, self.dest_node)


class ASTBranch:
    def __init__(self, expression_node, jump_if_true, offset_test, jump_to_label) -> None:
        self.expression_node = expression_node
        self.jump_if_true = jump_if_true
        self.offset_test = offset_test
        self.jump_to_label = jump_to_label

    def __repr__(self) -> str:
        if self.jump_if_true:
            return 'ASTBranch(if %s: jump #L%s)' % (self.expression_node, self.jump_to_label)
        else:
            return 'ASTBranch(if not %s: jump #L%s)' % (self.expression_node, self.jump_to_label)


class ASTJump:
    def __init__(self, offset_test, jump_to_label) -> None:
        self.offset_test = offset_test
        self.jump_to_label = jump_to_label

    def __repr__(self) -> str:
        return 'ASTJump(jump #L%s)' % self.jump_to_label


class ASTName:
    def __init__(self, name):
        self.name = name

    def __repr__(self) -> str:
        return 'ASTName(%s)' % self.name


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

    def __repr__(self) -> str:
        return 'ASTReturn(%s)' % self.value


class ASTCall:
    def __init__(self, func, pparams, kwparams) -> None:
        self.func = func
        self.pparams = pparams
        self.kwparams = kwparams

    def __repr__(self) -> str:
        return 'ASTCall(%s, %s, %s)' % (self.func, self.pparams, self.kwparams)


class ASTBinary:
    def __init__(self, left, right, op, op_str) -> None:
        self.left = left
        self.right = right
        self.op = op
        self.op_str = op_str

    def __repr__(self) -> str:
        return 'ASTBinary(%s %s %s)' % (self.left, self.op, self.right)


class ASTTuple:
    def __init__(self, values) -> None:
        self.values = values

    def __repr__(self) -> str:
        return 'ASTTuple(%s)' % self.values


class ASTSubscr:
    def __init__(self, name, key) -> None:
        self.name = name
        self.key = key

    def __repr__(self) -> str:
        return 'ASTSubscr(%s[%s])' % (self.name, self.key)


class ASTMap:
    def __init__(self, target_size) -> None:
        self.kv_pairs = []
        self.target_size = target_size

    def __repr__(self) -> str:
        return 'ASTMap(%s, target_size=%s)' % (self.kv_pairs, self.target_size)


class ASTLoadBuildClass:
    def __init__(self) -> None:
        pass

    def __repr__(self) -> str:
        return "ASTLoadBuildClass()"

# bases..


class ASTClass:
    def __init__(self, class_body_call, name) -> None:
        self.class_body_call = class_body_call
        self.name = name


class BlockSplitCodeLine:
    pass


class CodeLine:
    def __init__(self, ip, size, opcode, opcode_str, arg) -> None:
        self.ip = ip
        self.size = size
        self.opcode = opcode
        self.opcode_str = opcode_str
        self.arg = arg
        self.is_jump_target = False
        self.label = None
        self.jump_to_label = None

    def __repr__(self) -> str:
        return 'CodeLine(is_jump_target=%s, label=%s, ip=%s, size=%s, opcode=%s, opcode_str=%s, arg=%s, jump_to_label=%s)' % (self.is_jump_target, self.label, self.ip, self.size, self.opcode, self.opcode_str, self.arg, self.jump_to_label)

class ASTBlockNoOp:
    def __init__(self) -> None:
        pass

    def __repr__(self) -> str:
        return 'ASTBlockNoOp()'

class ASTLabel:
    def __init__(self, label) -> None:
        self.label = label

    def __repr__(self) -> str:
        return 'ASTLabel(label=#L%s)' %(self.label)

class CodeInfo:
    def __init__(self, func_name, code_lines, func_args) -> None:
        self.func_name = func_name
        self.func_args = func_args
        self.code_lines = code_lines

    def __repr__(self) -> str:
        return 'CodeInfo(%s, %s, code_length=%s)' % (self.func_args, self.func_args, len(self.code_lines))


g_ast_dict = {}
g_func_args_dict = {}
