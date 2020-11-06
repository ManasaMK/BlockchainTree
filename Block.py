import datetime
import hashlib
def print_tree(current_node, childattr='next', nameattr='data', indent='', last='updown'):
name = lambda node: getattr(node, nameattr)
children = lambda node: getattr(node, childattr)
nb_children = lambda node: sum(nb_children(child) for child in children(node)) + 1
size_branch = {child: nb_children(child) for child in children(current_node)}

""" Creation of balanced lists for "up" branch and "down" branch. """
up = sorted(children(current_node), key=lambda node: nb_children(node))
down = []
while up and sum(size_branch[node] for node in down) < sum(size_branch[node] for node in up):
down.append(up.pop())
""" Printing of "up" branch. """
for child in up:    
next_last = 'up' if up.index(child) is 0 else ''
next_indent = '{0}{1}{2}'.format(indent, ' ' if 'up' in last else '│', ' ' * len(name(current_node)))
print_tree(child, childattr, nameattr, next_indent, next_last)

""" Printing of current node. """
if last == 'up': start_shape = '┌'
elif last == 'down': start_shape = '└'
elif last == 'updown': start_shape = ' '
else: start_shape = '├'

if up: end_shape = '┤'
elif down: end_shape = '┐'
else: end_shape = ''

print('{0}{1}{2}{3}'.format(indent, start_shape, name(current_node), end_shape))

""" Printing of "down" branch. """
for child in down:
next_last = 'down' if down.index(child) is len(down) - 1 else ''
next_indent = '{0}{1}{2}'.format(indent, ' ' if 'down' in last else '│', ' ' * len(name(current_node)))
print_tree(child, childattr, nameattr, next_indent, next_last)

class Block:
blockNo = 0
data = None
next = []
nextBlock = []
hash = None
nonce = 0
previous_hash = 0x0
timestamp = datetime.datetime.now()

def __init__(self, data):
self.data = data
self.next = list()
self.nextBlock = list()

def hash(self):
h = hashlib.sha256()
h.update(
str(self.nonce).encode('utf-8') +
str(self.data).encode('utf-8') +
str(self.previous_hash).encode('utf-8') +
str(self.timestamp).encode('utf-8') +
str(self.blockNo).encode('utf-8')
)
return h.hexdigest()

def __str__(self):
return "Block Hash: " + str(self.hash()) + "\nBlockNo: " + str(self.blockNo) + "\nBlock Data: " + str(self.data) + "\nNext Block Data: " + str(self.nextBlock) + "\nHashes: " + str(self.nonce) + "\n--------------"

class Blockchain:

diff = 5
maxNonce = 2**32
target = 2 ** (256-diff)

block = Block("Head Block")
dummy = head = block

def add(self, block, previousBlock):

block.previous_hash = previousBlock.hash()
block.blockNo = self.block.blockNo + 1

previousBlock.next.append(block)
previousBlock.nextBlock.append(block.data)
self.block = block

def mine(self, block):
dummy = previousBlock = self.head
val = int(input("\nEnter the block to which data is to be added (0-"+str(self.block.blockNo)+"): "))
parser=self.head.next.copy()
while len(parser) != 0:
current = parser.pop()
if(current.blockNo==val):
dummy = previousBlock=current
print("\nFound\n")
break
parser.extend(current.next)
for n in range(self.maxNonce):
if int(block.hash(), 16) <= self.target:
self.add(block, previousBlock)
print("New Block:\n--------------")
print(block)
print("Previous Block:\n--------------")
print(previousBlock)
break
else:
block.nonce += 1

blockchain = Blockchain()

for n in range(10):
blockchain.mine(Block("Block " + str(n+1)))

print("\n\n--------------\n PRINTING\n--------------\n")
print_tree(blockchain.head)
print("\n--------------")
print(blockchain.head)
list=blockchain.head.next.copy()
while len(list) != 0:
btp = list.pop()
print(btp)
list.extend(btp.next)
