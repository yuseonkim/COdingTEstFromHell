package org.example.Programmers.LV3.표편집;

import java.util.Stack;

class Node {
    int position;
    Node prev, next;

    public Node(int position) {
        this.position = position;
    }
}

public class Solution {
    public static String solution(int n, int k, String[] cmds) {
        Node[] nodeArray = new Node[n];
        for (int i = 0; i < n; i++) {
            nodeArray[i] = new Node(i);
            if (i > 0) {
                nodeArray[i - 1].next = nodeArray[i];
                nodeArray[i].prev = nodeArray[i - 1];
            }
        }

        Stack<Node> removedNodes = new Stack<>();
        Node curr = nodeArray[k];

        for (String cmd : cmds) {
            String[] parts = cmd.split(" ");
            switch (parts[0]) {
                case "U":
                    for (int i = 0; i < Integer.parseInt(parts[1]); i++) {
                        curr = curr.prev;
                    }
                    break;
                case "D":
                    for (int i = 0; i < Integer.parseInt(parts[1]); i++) {
                        curr = curr.next;
                    }
                    break;
                case "C":
                    removedNodes.push(curr);
                    Node prev = curr.prev;
                    Node next = curr.next;
                    if (prev != null) prev.next = next;
                    if (next != null) next.prev = prev;
                    curr = next != null ? next : prev;
                    break;
                case "Z":
                    Node node = removedNodes.pop();
                    if (node.prev != null) node.prev.next = node;
                    if (node.next != null) node.next.prev = node;
                    break;
            }
        }

        StringBuilder sb = new StringBuilder("O".repeat(n));
        while (!removedNodes.isEmpty()) {
            sb.setCharAt(removedNodes.pop().position, 'X');
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        int n = 8;
        int k = 2;
        String[] cmd = {"D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"};
        String result = solution(n, k, cmd);
        System.out.println(result);
    }
}
