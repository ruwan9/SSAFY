import sys
sys.stdin = open('input_files/1991.txt')

# #################### 방법 1. ####################
# class Node:
#     def __init__(self, data, left_node, right_node):
#         self.data = data
#         self.left_node = left_node
#         self.right_node = right_node
#
#
# def pre_order(node):
#     print(node.data, end='')
#     if node.left_node != '.':
#         pre_order(tree[node.left_node])
#     if node.right_node != '.':
#         pre_order(tree[node.right_node])
#
#
# def in_order(node):
#     if node.left_node != '.':
#         in_order(tree[node.left_node])
#     print(node.data, end='')
#     if node.right_node != '.':
#         in_order(tree[node.right_node])
#
#
# def post_order(node):
#     if node.left_node != '.':
#         post_order(tree[node.left_node])
#     if node.right_node != '.':
#         post_order(tree[node.right_node])
#     print(node.data, end='')
#
#
# N = int(input())
# tree = {}  # dictionary형 자료형
# for i in range(N):
#     data, left_node, right_node = input().split()
#     tree[data] = Node(data, left_node, right_node)
#
# print(tree)
# pre_order(tree['A'])
# print()
# in_order(tree['A'])
# print()
# post_order(tree['A'])


"""
전위순회(pre): 루트 - 왼쪽 자식 - 오른쪽 자식
중위순회(mid): 왼쪽 자식 - 루트 - 오른쪽 자식
후위순회(post): 왼쪽 자식 - 오른쪽 자식 - 루트
"""


#################### 방법 2. ####################
# 전위: 루트 - 왼쪽 - 오른쪽
def preorder(node):
    if node == '.':
        return
    print(node, end='')
    preorder(tree[node][0]) # tree[key][value], 왼쪽 자식 노드
    preorder(tree[node][1]) # 오른쪽 자식 노드


# 중위: 왼쪽 - 루트 - 오른쪽
def inorder(node):
    if node == '.':
        return
    inorder(tree[node][0]) # 왼쪽 자식 노드
    print(node, end='')
    inorder(tree[node][1]) # 오른쪽 자식 노드


# 후위: 왼쪽 - 오른쪽 - 루트
def postorder(node):
    if node == '.':
        return
    postorder(tree[node][0]) # 왼쪽 자식 노드
    postorder(tree[node][1]) # 오른쪽 자식 노드
    print(node, end='')


n = int(input())
tree = {}

# tree 만들기
for _ in range(n):
    root, left, right = input().split()
    tree[root] = (left, right)

# print(tree)
preorder('A')
print()
inorder('A')
print()
postorder('A')
